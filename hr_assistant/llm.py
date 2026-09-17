"""step 6. connect  to the llm"""

from langchain_groq import ChatGroq
from hr_assistant import config
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """return a chat model. reads groq api key from the environment"""
    return ChatGroq(model = config.LLM_MODEL_NAME, temperature = 0)