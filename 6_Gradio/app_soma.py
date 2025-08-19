import gradio as gr


def somar(num1, num2):
    return num1 + num2


iface = gr.Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs="number",
    title="Soma de dois números",
    description="Faça a soma de dois números",
    theme="dark",
)
iface.launch()
