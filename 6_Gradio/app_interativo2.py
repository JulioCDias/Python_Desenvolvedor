import gradio as gr 
import string
from collections import Counter

def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])
    return num_palavras, num_caracteres, frequencia_html


iface = gr.Interface(
    fn=analisar_texto,
    inputs=gr.Textbox(
        gr.Textbox(
            label="Texto",
            placeholder="Digite ou cole seu texto aqui...",
            lines=10,
        ),
    ),
    outputs=[
        gr.Number(label="Número de Palavras"),
        gr.Number(label="Número de Caracteres"),
        gr.HTML(label="Frequência de Palavras"),
    ],
    title="Analisador de Texto",
    description="Analisa o texto fornecido e retorna o número de palavras, número de caracteres e a frequência de cada palavra.",
)

iface.launch()