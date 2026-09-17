from langchain_community.document_loaders import TextLoader
from hr_assistant import config


def load_documents(file_path: str = config.DATA_FILE_PATH):
    """ Load a .txt file and return a list of langchain documents"""
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()