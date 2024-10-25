import os
import random
import string
import sys
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import shutil


# Set OpenAI API key
#os.environ["OPENAI_API_KEY"] = ''

def generate_random_filename(length=10):
    """Generate a random filename with the given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length)) + '.md'

def main():
    # Generate a random filename
    random_filename = generate_random_filename()

    # Construct the command
    command = f"code2prompt --path ./write.html --path ./dashboard.html --path ./app.py --suppress-comments --tokens --encoding cl100k_base --output {random_filename}"

    # Run the command
    exit_code = os.system(command)

    if exit_code == 0:
        print(f"Command executed successfully. Output saved to {random_filename}")

        sys.exit(0)  # Exit with success status
    else:
        print(f"An error occurred while executing the command. Exit code: {exit_code}")
        sys.exit(1)  # Exit with error status

if __name__ == "__main__":
    main()