import gradio as gr


def reverter_texto(texto):
    texto_reverso = texto[::-1]
    return texto_reverso, len(texto_reverso)


iface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title="Reversor de Texto",
    description="Reverte o texto e conta a quantidade de caracteres",
)
iface.launch()
