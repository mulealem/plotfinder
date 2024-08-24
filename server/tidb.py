from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import TiDBVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
import requests
from langchain_community.embeddings import JinaEmbeddings
from numpy import dot
from numpy.linalg import norm
from PIL import Image

from tmdb_movie_search import get_movie_by_id

# replace YOUR_JINA_API_KEY with your actual Jina API key
embeddings = JinaEmbeddings(
    jina_api_key="YOUR_JINA_API_KEY", model_name="jina-embeddings-v2-base-en"
)

# replace YOUR_TIDB_CONNECTION_STRING with your actual TiDB connection string
tidb_connection_string = "YOUR_TIDB_CONNECTION_STRING"


# replace YOUR_TABLE_NAME with your actual table name
TABLE_NAME = "YOUR_TABLE_NAME"
db = TiDBVectorStore.from_existing_vector_table(
    embedding=embeddings,
    table_name=TABLE_NAME,
    connection_string=tidb_connection_string,
    distance_strategy="cosine",  # default, another option is "l2"
)

def query_db(query):
    docs_with_score = db.similarity_search_with_score(query, k=15)
    metadatas = []
    for doc, score in docs_with_score:
        movie_id = doc.metadata["id"]
        movie = get_movie_by_id(movie_id)
        metadatas.append({
            "metadata": movie,
            "content": doc.page_content,
            "score": score
        })
    return metadatas
