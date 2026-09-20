"""step 6. connect  to the llm"""

from langchain_groq import ChatGroq
from hr_assistant import config
from dotenv import load_dotenv
from hr_assistant.logger import get_logger

load_dotenv()

logger = get_logger(__name__)

def get_llm():
    """return a chat model. reads groq api key from the environment"""
    logger.info("Initializing LLM %s", config.LLM_MODEL_NAME)
    return ChatGroq(model = config.LLM_MODEL_NAME, temperature = 0)