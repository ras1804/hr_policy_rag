"""step 3. turn text into numbers (vectors) using Jina"""

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from dotenv import load_dotenv

load_dotenv()


def get_embeddings_model():
    """return a jina embeddings model.
    Reads JINA_API_KEY from the environment"""
    return JinaEmbeddings(model_name = config.EMBEDDING_MODEL_NAME)

