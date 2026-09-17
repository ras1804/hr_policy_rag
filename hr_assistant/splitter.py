"""step 2. chop the document into small, searchable chunks"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config
from hr_assistant.document_loader import load_documents
from dotenv import load_dotenv

load_dotenv()


# def split_into_chunks(chunk_size: int = config.CHUNK_SIZE, chunk_overlap: int = config.CHUNK_OVERLAP):
#     """"split documents into small overlapping chunks"""

#     documents = load_documents()
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size = chunk_size,
#         chunk_overlap = chunk_overlap
#     )
#     return text_splitter.split_text(documents[0].page_content)



def split_into_chunks(documents):
    """"split documents into small overlapping chunks"""

    chunk_size = config.CHUNK_SIZE
    chunk_overlap = config.CHUNK_OVERLAP
    # chunk_overlap = chunk_overlap
    # documents = load_documents()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )
    return text_splitter.split_documents(documents)