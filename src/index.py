# Função para processar o arquivo enviado
def process_file(file):
	if file is None:
		return "Nenhum arquivo enviado."
	return f"Arquivo recebido: {file.name}"