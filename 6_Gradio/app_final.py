import gradio as gr
import string
from collections import Counter

def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9
    

def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])
    return num_palavras, num_caracteres, frequencia_html


def criar_relatorio(temperatura, escala, texto, condicao):
    temp_convertida = converter_temperatura(temperatura, escala)
    num_palavras, num_caracteres, frequencia_html = analisar_texto(texto)
    relatorio = (f"""
    <h2>Relatório de Análise</h2>
    <p><strong>Temperatura Convertida:</strong> {temp_convertida:.2f} {'Celsius' if escala == 'Fahrenheit' else 'Fahrenheit'}</p>
    <p><strong>Condição:</strong> {condicao}</p>
    <p><strong>Número de Palavras:</strong> {num_palavras}</p>
    <p><strong>Número de Caracteres:</strong> {num_caracteres}</p>
    <div><strong>Frequência de Palavras:</strong><br>{frequencia_html}</div>
    """)
    return relatorio

iface = gr.Interface(
    fn=criar_relatorio,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(
            choices=["Celsius", "Fahrenheit"],
            label="Converter De:",
        ),
        gr.Dropdown(
            choices=["Ensolarado", "Nublado", "Chuvoso", "Frio", "Quente"],
            label="Condição do Tempo",
        ),
        gr.Textbox(
            label="Descrição do Tempo",
            placeholder="Descreva o tempo atual...",
            lines=5,
        ),
    ],
    outputs=gr.Markdown(label="Relatório de Análise"),
    title="Conversor e Analisador de Texto",
    description="Converte temperaturas e analisa textos, gerando um relatório detalhado.",
)
iface.launch()
        