'''Modulo para indexação de documentos e extração de informações.'''

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def process_file(file):
    '''Função para processar o arquivo enviado e extrair informações.'''

    if file is None:
        return "Nenhum arquivo enviado."

    loader = PyMuPDFLoader(file)
    document = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    embeddings = HuggingFaceEmbeddings()
    docsearch = Chroma.from_documents(
        texts, embeddings, persist_directory="./chroma_db")

    return f"Arquivo recebido: {file.name}\n\n{texts}"
