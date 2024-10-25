# Table of Contents
- write.html
- dashboard.html
- app.py

## File: write.html

- Extension: .html
- Language: html
- Size: 10705 bytes
- Created: 2024-10-24 15:21:57
- Modified: 2024-10-24 15:21:57

### Code

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Kenny Sadiku Blog</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <meta content="Kenny Sadiku Blog" name="keywords" />
    <meta content="Kenny Sadiku Blog" name="description" />

    
    <link href="static/img/favicon.ico" rel="icon" />

    
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:300;400;600;700;800&display=swap"
      rel="stylesheet"
    />

    
    <link
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css"
      rel="stylesheet"
    />

    
    <link
      href="{{ url_for('static', path='css/style.css') }}"
      rel="stylesheet"
    />

    
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css"
    />
    <script src="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js"></script>

    
    <style>
      .loading {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.8);
        z-index: 1000;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      .spinner {
        border: 8px solid #f3f3f3; /* Light grey */
        border-top: 8px solid #3498db; /* Blue */
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 1s linear infinite;
      }

      @keyframes spin {
        0% {
          transform: rotate(0deg);
        }
        100% {
          transform: rotate(360deg);
        }
      }

      .editor-preview-side {
        top: 50px;
        right: 0;
        bottom: 0;
        width: 50%;
        overflow: auto;
        background: #fff;
        z-index: 1000;
      }
      .editor-toolbar {
        background-color: #f8f9fa;
        border-radius: 0;
      }
      .CodeMirror {
        height: calc(100vh - 200px);
      }
      .editor-statusbar {
        padding: 8px 15px;
        background-color: #f8f9fa;
        color: #6c757d;
      }
    </style>
  </head>

  <body>
    <div class="wrapper">
      <div class="sidebar">
        <div
          class="sidebar-text d-flex flex-column h-100 justify-content-center text-center"
        >
          <img
            class="mx-auto d-block w-75 bg-primary img-fluid rounded-circle mb-4 p-3"
            src="{{ url_for('static', path='img/profile.jpg') }}"
            alt="Image"
          />
          <h1 class="font-weight-bold">Kenny Sadiku</h1>
          <p class="mb-4">
            A vsionary writer with great abilities in crafting insprational and
            christian content
          </p>
          <div class="d-flex justify-content-center mb-5">
            <a class="btn btn-outline-primary mr-2" href="#"
              ><i class="fab fa-twitter"></i
            ></a>
            <a class="btn btn-outline-primary mr-2" href="#"
              ><i class="fab fa-facebook-f"></i
            ></a>
            <a class="btn btn-outline-primary mr-2" href="#"
              ><i class="fab fa-linkedin-in"></i
            ></a>
            <a class="btn btn-outline-primary mr-2" href="#"
              ><i class="fab fa-instagram"></i
            ></a>
          </div>
          <a href="/about" class="btn btn-lg btn-block btn-primary mt-auto"
            >About Me</a
          >
        </div>
        <div
          class="sidebar-icon d-flex flex-column h-100 justify-content-center text-right"
        >
          <i class="fas fa-2x fa-angle-double-right text-primary"></i>
        </div>
      </div>
      <div class="content">
        
        <div class="container p-0">
          <nav class="navbar navbar-expand-lg bg-secondary navbar-dark">
            <a href="" class="navbar-brand d-block d-lg-none">Navigation</a>
            <button
              type="button"
              class="navbar-toggler"
              data-toggle="collapse"
              data-target="#navbarCollapse"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
            <div
              class="collapse navbar-collapse justify-content-between"
              id="navbarCollapse"
            >
              <div class="navbar-nav m-auto">
                <a href="/" class="nav-item nav-link">Home</a>
                <a href="/about" class="nav-item nav-link">About</a>
                <a href="/blog" class="nav-item nav-link">Blog</a>
                <a href="/contact" class="nav-item nav-link">Contact</a>
                <a href="/dashboard" class="nav-item nav-link">Dashboard</a>
              </div>
            </div>
          </nav>
        </div>
        

        
        <div class="container py-5 px-2 bg-primary">
          <div class="row py-5 px-4">
            <div class="col-sm-6 text-center text-md-left">
              <h1
                class="mb-3 mb-md-0 text-white text-uppercase font-weight-bold"
              >
                Write Blog Post
              </h1>
            </div>
            <div class="col-sm-6 text-center text-md-right">
              <div class="d-inline-flex pt-2">
                <h4 class="m-0 text-white">
                  <a class="text-white" href="">Home</a>
                </h4>
                <h4 class="m-0 text-white px-2">/</h4>
                <h4 class="m-0 text-white">Write Blog Post</h4>
              </div>
            </div>
          </div>
        </div>
        

        
        <div id="loading" class="loading" style="display: none">
          <div class="spinner"></div>
        </div>

        
        <div class="container py-5 px-2 bg-white">
          <div class="row px-4">
            <div class="col-12 mb-3">
              <input
                type="text"
                id="title"
                class="form-control form-control-lg"
                placeholder="Enter your blog title"
              />
            </div>
            <div class="col-12 mb-3">
              <input
                type="text"
                id="image"
                class="form-control form-control-lg"
                placeholder="Enter the image of your blog"
              />
            </div>
            <div class="col-12">
              <textarea id="editor"></textarea>
            </div>
          </div>
          <div class="row px-4 mt-4">
            <div class="col-12">
              <button id="publishButton" class="btn btn-primary">
                Publish Post
              </button>
              <button id="saveButton" class="btn btn-primary">Save</button>
            </div>
          </div>
        </div>
        

        
        <div class="container py-4 bg-secondary text-center">
          <p class="m-0 text-white">
            &copy;
            <a class="text-white font-weight-bold" href="#">Kenny Sadiku</a>.
            All Rights Reserved
          </p>
        </div>
        
      </div>
    </div>

    
    <a href="#" class="back-to-top"><i class="fa fa-angle-double-up"></i></a>

    
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', path='lib/easing/easing.min.js') }}"></script>
    <script src="{{ url_for('static', path='lib/waypoints/waypoints.min.js') }}"></script>

    
    <script src="{{ url_for('static', path='mail/jqBootstrapValidation.min.js') }}"></script>
    <script src="{{ url_for('static', path='mail/contact.js') }}"></script>

    
    <script src="{{ url_for('static', path='js/main.js') }}"></script>
    <script>
      var simplemde = new SimpleMDE({
        element: document.getElementById("editor"),
        spellChecker: false,
        autosave: {
          enabled: true,
          unique_id: "blogPost",
        },
      });

      // Helper function to show/hide loading spinner
      function toggleLoading(show) {
        const loadingElement = document.getElementById("loading");
        loadingElement.style.display = show ? "flex" : "none";
      }

      // Helper function to send POST request to backend
      async function submitPost(actionType) {
        var title = document.getElementById("title").value;
        var image = document.getElementById("image").value;
        var content = simplemde.value();

        if (!title || !content) {
          alert("Title and Content are required");
          return;
        }

        try {
          // Show loading spinner
          toggleLoading(true);

          // Disable buttons while submitting
          document.getElementById("publishButton").disabled = true;
          document.getElementById("saveButton").disabled = true;

          const response = await fetch("/dashboard/write", {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
              title: title,
              image: image,
              body: content,
              action: actionType,
            }),
          });

          if (response.redirected) {
            window.location.href = response.url;
          } else {
            const data = await response.json();
            console.log("Success:", data);
          }
        } catch (error) {
          console.error("Error:", error);
          alert(
            "An error occurred while submitting the post. Please try again."
          );
        } finally {
          // Hide loading spinner and re-enable buttons
          toggleLoading(false);
          document.getElementById("publishButton").disabled = false;
          document.getElementById("saveButton").disabled = false;
        }
      }

      // Handle "Publish" button click
      document
        .getElementById("publishButton")
        .addEventListener("click", function () {
          submitPost("Publish");
        });

      // Handle "Save" button click
      document
        .getElementById("saveButton")
        .addEventListener("click", function () {
          submitPost("Save");
        });
    </script>
  </body>
</html>

```

## File: dashboard.html

- Extension: .html
- Language: html
- Size: 8708 bytes
- Created: 2024-10-24 16:54:53
- Modified: 2024-10-24 16:54:53

### Code

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Kenny Sadiku Blog</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="Kenny Sadiku Blog" name="keywords">
    <meta content="Kenny Sadiku Blog" name="description">

    
    <link href="static/img/favicon.ico" rel="icon">

    
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:300;400;600;700;800&display=swap" rel="stylesheet">

    
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">

    
    <link href="{{ url_for('static', path='css/style.css') }}" rel="stylesheet">

    
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    
    <style>
        .published-icon {
            font-size: 1.5rem;
            color: green;
        }

        .saved-icon {
            font-size: 1.5rem;
            color: orange;
        }

        .table-wrapper {
            margin-top: 30px;
        }

        .graph-wrapper {
            margin-top: 50px;
        }

        .action-btn {
            border-radius: 20px;
            padding: 10px 20px;
            font-size: 0.9rem;
            font-weight: bold;
        }

        .btn-edit {
            background-color: #f0ad4e;
            color: white;
        }

        .btn-edit:hover {
            background-color: #ec971f;
            color: white;
        }

        .btn-delete {
            background-color: #d9534f;
            color: white;
        }

        .btn-delete:hover {
            background-color: #c9302c;
            color: white;
        }

        .btn-write-new {
            background-color: #5cb85c;
            color: white;
            border-radius: 20px;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: bold;
        }

        .btn-write-new:hover {
            background-color: #4cae4c;
            color: white;
        }

        canvas {
            max-width: 100%;
            height: 400px;
        }

        .sidebar-text {
            margin-bottom: 20px;
        }
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="sidebar">
            <div class="sidebar-text d-flex flex-column h-100 justify-content-center text-center">
                <img class="mx-auto d-block w-75 bg-primary img-fluid rounded-circle mb-4 p-3"
                    src="{{ url_for('static', path='img/profile.jpg') }}" alt="Image">
                <h1 class="font-weight-bold">Kenny Sadiku</h1>
                <p>A visionary writer crafting inspirational and Christian content.</p>
                <div class="d-flex justify-content-center mb-5">
                    <a class="btn btn-outline-primary mr-2" href="#"><i class="fab fa-twitter"></i></a>
                    <a class="btn btn-outline-primary mr-2" href="#"><i class="fab fa-facebook-f"></i></a>
                    <a class="btn btn-outline-primary mr-2" href="#"><i class="fab fa-linkedin-in"></i></a>
                    <a class="btn btn-outline-primary mr-2" href="#"><i class="fab fa-instagram"></i></a>
                </div>
                <a href="/about" class="btn btn-lg btn-block btn-primary mt-auto">About Me</a>
            </div>
        </div>
        <div class="content">
            
            <div class="container p-0">
                <nav class="navbar navbar-expand-lg bg-secondary navbar-dark">
                    <div class="navbar-nav m-auto">
                        <a href="/" class="nav-item nav-link">Home</a>
                        <a href="/about" class="nav-item nav-link">About</a>
                        <a href="/blog" class="nav-item nav-link">Blog</a>
                        <a href="/contact" class="nav-item nav-link">Contact</a>
                        <a href="/dashboard/write" class="nav-item nav-link">Write</a>
                    </div>
                </nav>
            </div>
            

            
            <div class="container py-5">
                <h1 class="mb-4 text-center">Blog Articles Dashboard</h1>

                
                <div class="text-center mb-4">
                    <a href="/dashboard/write" class="btn btn-write-new">Write New Article</a>
                </div>

                <div class="table-wrapper">
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>Title</th>
                                <th>Published</th>
                                <th>Readers</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for article in articles %}
                            <tr>
                                <td>{{ article.data.title }}</td>
                                <td>
                                    {% if article.data.publish_status %}
                                        <i class="fas fa-check-circle published-icon"></i>
                                    {% else %}
                                        <i class="fas fa-save saved-icon"></i>
                                    {% endif %}
                                </td>
                                <td>{{ article.data.readers_count | default(0) }}</td> 
                                <td>
                                    <div class="d-flex">
                                        <a href="/dashboard/edit/{{ article.data.id }}" class="btn action-btn btn-edit mr-2">Edit</a>
                                        <form method="post" action="/dashboard/delete/{{ article.data.id }}" style="display:inline;">
                                            <button class="btn action-btn btn-delete" type="submit">Delete</button>
                                        </form>
                                    </div>
                                </td>
                                
                            </tr>
                            {% endfor %}
                        </tbody>
                        
                    </table>
                </div>

                <div class="graph-wrapper">
                    <h2 class="mb-4 text-center">Website Metrics</h2>
                    <canvas id="metricsChart"></canvas>
                </div>
            </div>
            

            
            <div class="container py-4 bg-secondary text-center">
                <p class="m-0 text-white">
                    &copy; <a class="text-white font-weight-bold" href="#">Kenny Sadiku</a>. All Rights Reserved
                </p>
            </div>
            
        </div>
    </div>

    
    <a href="#" class="back-to-top"><i class="fa fa-angle-double-up"></i></a>

    
    <script>
        var ctx = document.getElementById('metricsChart').getContext('2d');
        var metricsChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Total Visitors', 'Unique Visitors', 'Articles Published', 'Readers'],
                datasets: [{
                    label: 'Website Metrics',
                    data: [1500, 1200, 5, 300], // Example data
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    </script>

    
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>

</body>

</html>

```

## File: app.py

- Extension: .py
- Language: python
- Size: 9669 bytes
- Created: 2024-10-24 16:55:01
- Modified: 2024-10-24 16:55:01

### Code

```python
from fastapi import FastAPI, Request, Form, HTTPException, Query
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

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="./")

load_dotenv()

client = FaunaClient(secret=os.getenv("FAUNA_SECRET_KEY"))



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        
        articles = client.query(
            q.map_(
                lambda x: q.get(x),
                q.paginate(
                    q.documents(q.collection("blog_articles")),
                    size=6
                )
            )
        )
        
        
        article_list = [
            {
                "id": article["data"]["id"],
                "title": article["data"]["title"],
                "image": article["data"]["image"],
                "body": article["data"]["body"],
                "publish_status": article["data"]["publish_status"]
            }
            for article in articles["data"]
            if article["data"]["publish_status"]  
        ]
        
        
        carousel_articles = article_list[:3]
        
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
        
        result = client.query(
            q.map_(
                lambda x: q.get(x),
                q.paginate(
                    q.documents(q.collection("blog_articles")),
                    size=100000  
                )
            )
        )
        
        
        published_articles = [
            doc for doc in result["data"] 
            if doc["data"].get("publish_status", False) is True
        ]
        
        
        total_count = len(published_articles)
        
        
        start_idx = skip
        end_idx = start_idx + per_page
        paginated_articles = published_articles[start_idx:end_idx]
        
        
        articles = [
            {
                "id": doc["data"]["id"],
                "title": doc["data"]["title"],
                "image": doc["data"]["image"],
                "body": doc["data"]["body"][:200] + "..." 
            }
            for doc in paginated_articles
        ]
        
        
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
    
    article = get_blog_article_by_id(id)
    
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    

    
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
async def test(request: Request):
    return templates.TemplateResponse("write.html", {"request": request})

@app.post("/dashboard/write")
async def write_article(request: Request, title: str = Form(), body: str = Form(), image: str = Form(), action: str = Form()):
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

    
    return RedirectResponse("/dashboard", status_code=303)



@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    
    articles = client.query(q.paginate(q.documents(q.collection("blog_articles"))))
    
    
    article_data = [client.query(q.get(ref)) for ref in articles['data']]
    
    return templates.TemplateResponse("dashboard.html", {"request": request, "articles": article_data})





@app.get("/dashboard/edit/{article_id}", response_class=HTMLResponse)
async def edit_article_page(request: Request, article_id: str):
    try:
        
        article = client.query(
            q.get(q.match(q.index("article_by_id"), article_id))
        )
        
        
        article_data = {
            "id": article["data"]["id"],  
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
    action: str = Form(...)
):
    try:
        
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
async def delete_article(article_id: str):
    try:
        
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
   uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
```

