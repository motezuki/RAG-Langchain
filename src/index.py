from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Função para processar o arquivo enviado
def process_file(file):
	if file is None:
		return "Nenhum arquivo enviado."
	loader = PyMuPDFLoader(file)
	document = loader.load()
	text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
	texts = text_splitter.split_documents(document)

	return f"Arquivo recebido: {file.name}\n{texts}"