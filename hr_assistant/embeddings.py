"""step 3. turn text into numbers (vectors) using Jina"""

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from dotenv import load_dotenv
from hr_assistant.logger import get_logger

load_dotenv()

logger = get_logger(__name__)

def get_embeddings_model():
    """return a jina embeddings model.
    Reads JINA_API_KEY from the environment"""
    logger.info("Initializing the embedding model %s", config.EMBEDDING_MODEL_NAME)
    return JinaEmbeddings(model_name = config.EMBEDDING_MODEL_NAME)

