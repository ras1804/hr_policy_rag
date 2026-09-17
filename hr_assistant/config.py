"ALL settings for the app live here, in one place."

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")


# define path of data and vector store

DATA_FILE_PATH = Path("data.txt")
VECTOR_STORE_PATH = Path("faiss_index")


#llm and embedding model settings

LLM_MODEL_NAME = "openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"


# chunk/text splitting config

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

 
# retrieval results
TOP_K_RESULTS = 3


# system instructions

SYSTEM_PROMPT = (
    "You are a friendly HR assistant, "
    "Always use the search_hr_policy tool to look up the facts before answering. "
    "If the answer isn't in the search results, say you dont know instead of guessing."
)


def check_api_keys():
    """stop early with a clear message if a required API key is missing"""
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set. Please set it in the environment variables.")
    if not JINA_API_KEY:
        raise ValueError("JINA_API_KEY is not set. Please set it in the environment variables.")
