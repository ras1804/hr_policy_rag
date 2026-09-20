"""step 5. wrap the retriever as a tool the agent can call."""

from langchain.tools import tool
from dotenv import load_dotenv
from hr_assistant.logger import get_logger

load_dotenv()

logger = get_logger(__name__)


def create_search_tool(retriever):
    """return a @tool function that searches the HR policy document."""

    @tool 
    def search_hr_policy(question:str) -> str:
        """search the HR policy document for information about leave, work from home, probation, notice period, reimbursement, code of conduct, holidays or exit process"""
        logger.info("search_hr_policy called with query: %s", question)
        matching_chunks = retriever.invoke(question)
        logger.info("Found %d matching chunks", len(matching_chunks))
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)

    return search_hr_policy