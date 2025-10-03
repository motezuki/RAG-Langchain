import gradio as gr

def process_file(file):
	if file is None:
		return "Nenhum arquivo enviado."
	return f"Arquivo recebido: {file.name}"

# Função para chat (simples, apenas ecoa a mensagem)
def chat_fn(message, history):
	history = history or []
	response = f"Você disse: {message}"
	history.append((message, response))
	return "", history

with gr.Blocks() as demo:
	gr.Markdown("# RAG with Langchain and Gradio")
	with gr.Row():
		with gr.Column():
			file_input = gr.File(label="Envie um arquivo - RAG")
			file_output = gr.Textbox(label="Status do arquivo", lines=40)
			file_btn = gr.Button("Processar arquivo")
			file_btn.click(process_file, inputs=file_input, outputs=file_output)
		with gr.Column():
			gr.ChatInterface(chat_fn)

if __name__ == "__main__":
	demo.launch()