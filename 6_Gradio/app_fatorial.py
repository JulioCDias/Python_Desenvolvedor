import gradio as gr
import math


def fatorial(num):
    if num < 0:
        return "Fatoral nao defiido para numeros negtivos"
    return math.factorial(num)


iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="text",
    title="Fatorial",
    description="Calcula o fatorial de um numero",
)
iface.launch()
