from fastapi import FastAPI, Request, Form, HTTPException, Query
from fastapi import FastAPI, Request, Form, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.errors import NotFound
import json
import os
import uvicorn
from dotenv import load_dotenv
import math
import uuid
from passlib.context import CryptContext
import secrets


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Add these imports to your existing imports
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hardcoded credentials (in practice, these should be stored securely in a database)
CREDENTIALS = {
    "Kenny's Blog": {
        "hashed_password": pwd_context.hash("KennySadiku")
    }
}

async def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(
        credentials.username.encode("utf8"),
        "Kenny's Blog".encode("utf8")
    )
    is_password_correct = secrets.compare_digest(
        credentials.password.encode("utf8"),
        "KennySadiku".encode("utf8")
    )
    
    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


templates = Jinja2Templates(directory="./")

load_dotenv()

client = FaunaClient(secret=os.getenv("FAUNA_SECRET_KEY"))


# Add these new routes to your FastAPI app
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        # Fetch the last 6 published articles
        articles = client.query(
            q.map_(
                lambda x: q.get(x),
                q.paginate(
                    q.documents(q.collection("blog_articles")),
                    size=6
                )
            )
        )
        
        # Extract the data from the FaunaDB response
        article_list = [
            {
                "id": article["data"]["id"],
                "title": article["data"]["title"],
                "image": article["data"]["image"],
                "body": article["data"]["body"],
                "publish_status": article["data"]["publish_status"]
            }
            for article in articles["data"]
            if article["data"]["publish_status"]  # Only show published articles
        ]
        
        # Get the first 3 articles for the carousel
        carousel_articles = article_list[:3]
        # Get all 6 articles for the blog list
        blog_articles = article_list

        return templates.TemplateResponse(
            "index.html", 
            {
                "request": request,
                "carousel_articles": carousel_articles,
                "blog_articles": blog_articles
            }
        )
    except Exception as e:
        # Handle any errors and return an empty list if necessary
        return templates.TemplateResponse(
            "index.html", 
            {
                "request": request,
                "carousel_articles": [],
                "blog_articles": []
            }
        )


@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request, page: int = Query(1, ge=1)):
    per_page = 6
    skip = (page - 1) * per_page
    
    try:
        # First get all published articles
        result = client.query(
            q.map_(
                lambda x: q.get(x),
                q.paginate(
                    q.documents(q.collection("blog_articles")),
                    size=100000  # Set a large size to get all documents
                )
            )
        )
        
        # Filter published articles in Python
        published_articles = [
            doc for doc in result["data"] 
            if doc["data"].get("publish_status", False) is True
        ]
        
        # Calculate total count
        total_count = len(published_articles)
        
        # Handle pagination
        start_idx = skip
        end_idx = start_idx + per_page
        paginated_articles = published_articles[start_idx:end_idx]
        
        # Format articles for template
        articles = [
            {
                "id": doc["data"]["id"],
                "title": doc["data"]["title"],
                "image": doc["data"]["image"],
                "body": doc["data"]["body"][:200] + "..." # Truncate body for preview
            }
            for doc in paginated_articles
        ]
        
        # Calculate pagination info
        total_pages = math.ceil(total_count / per_page)
        has_next = page < total_pages
        has_prev = page > 1
        
        return templates.TemplateResponse(
            "blog.html",
            {
                "request": request,
                "articles": articles,
                "current_page": page,
                "total_pages": total_pages,
                "has_next": has_next,
                "has_prev": has_prev
            }
        )
    except Exception as e:
        print(f"Error: {e}")
        return templates.TemplateResponse(
            "blog.html",
            {
                "request": request,
                "articles": [],
                "error": f"Failed to fetch articles: {str(e)}"
            }
        )


def get_blog_article_by_id(article_id):
    try:
        result = client.query(
            q.get(q.match(q.index("article_by_id"), article_id))
        )
        return result['data']
    except NotFound:
        return None


@app.get("/blog/{id}", response_class=HTMLResponse)
async def display_blog_post(request: Request, id: str):
    # Fetch the article by its ID
    article = get_blog_article_by_id(id)
    
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    

    # Pass article data to the single.html template
    return templates.TemplateResponse("single.html", {
        "request": request,
        "title": article["title"],
        "image": article["image"],
        "markdown_content": article["body"]
    })


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/dashboard/write", response_class=HTMLResponse)
async def write_page(request: Request, username: str = Depends(authenticate_user)):
    return templates.TemplateResponse("write.html", {"request": request})

@app.post("/dashboard/write")
async def write_article(request: Request, username: str = Depends(authenticate_user), title: str = Form(), body: str = Form(), image: str = Form(), action: str = Form()):
    publish_status = True if action == "Publish" else False

    new_article = {
        "data": {
            "id": uuid.uuid4(),
            "title": title,
            "image": image,
            "publish_status": publish_status,
            "body": body
        }
    }
    
    client.query(q.create(q.collection("blog_articles"), new_article))

    # Redirect back to dashboard after submission
    return RedirectResponse("/dashboard", status_code=303)



@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, username: str = Depends(authenticate_user)):
    articles = client.query(q.paginate(q.documents(q.collection("blog_articles"))))
    article_data = [client.query(q.get(ref)) for ref in articles['data']]
    return templates.TemplateResponse("dashboard.html", {"request": request, "articles": article_data})



# Add these new endpoints to your existing app.py

@app.get("/dashboard/edit/{article_id}", response_class=HTMLResponse)
async def edit_article_page(request: Request, article_id: str, username: str = Depends(authenticate_user)):
    try:
        # Query FaunaDB using the custom id (article["data"]["id"])
        article = client.query(
            q.get(q.match(q.index("article_by_id"), article_id))
        )
        
        # Extract the custom id field correctly
        article_data = {
            "id": article["data"]["id"],  # Correct use of the custom "id" field
            "title": article["data"]["title"],
            "image": article["data"]["image"],
            "body": article["data"]["body"]
        }
        
        return templates.TemplateResponse("edit.html", {
            "request": request,
            "article": article_data
        })
    except NotFound:
        raise HTTPException(status_code=404, detail="Article not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/dashboard/edit/{article_id}")
async def update_article(
    article_id: str,
    title: str = Form(...),
    body: str = Form(...),
    image: str = Form(...),
    action: str = Form(...),
    username: str = Depends(authenticate_user)
):
    try:
        # Update the article in FaunaDB based on the custom "id"
        publish_status = True if action == "Publish" else False
        
        updated_article = client.query(
            q.update(
                q.select(
                    "ref",
                    q.get(q.match(q.index("article_by_id"), article_id))
                ),
                {
                    "data": {
                        "title": title,
                        "image": image,
                        "body": body,
                        "publish_status": publish_status
                    }
                }
            )
        )
        
        return RedirectResponse("/dashboard", status_code=303)
    except NotFound:
        raise HTTPException(status_code=404, detail="Article not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/dashboard/delete/{article_id}")
async def delete_article(article_id: str, username: str = Depends(authenticate_user)):
    try:
        # Delete the article based on the custom "id" field
        client.query(
            q.delete(
                q.select(
                    "ref",
                    q.get(q.match(q.index("article_by_id"), article_id))
                )
            )
        )
        
        return RedirectResponse("/dashboard", status_code=303)
    except NotFound:
        raise HTTPException(status_code=404, detail="Article not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
   uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
