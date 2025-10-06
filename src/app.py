''' Este app faz a leitura de um arquivo PDF e permite um chat simples com informações
extraídas do documento.'''

import gradio as gr
from indexing import process_file


def chat_fn(message, history):
    '''Função de chat simples que ecoa a mensagem do usuário.'''
    history = history or []
    response = f"Você disse: {message}"
    history.append((message, response))
    return "", history


with gr.Blocks() as demo:
    gr.Markdown("# RAG with Langchain and Gradio")
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="Envie um arquivo - RAG", file_types=['.pdf'])
            file_output = gr.Textbox(label="Status do arquivo", lines=40)
            file_btn = gr.Button("Processar arquivo")
            file_btn.click(process_file, inputs=file_input, # pylint: disable=no-member
                           outputs=[file_output])
        with gr.Column():
            gr.ChatInterface(chat_fn)

if __name__ == "__main__":
    demo.launch()
