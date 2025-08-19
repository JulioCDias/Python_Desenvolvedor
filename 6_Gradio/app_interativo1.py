import gradio as gr

def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        return (temperatura - 32) * 5/9
    else:
        return (temperatura * 9/5) + 32
    
iface = gr.Interface(
    fn=converter_temperatura,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(
            choices=["Celsius", "Fahrenheit"],
            label="Converter Para:"),
    ],
    outputs=gr.Number(label="Resultado"),
    title="Conversor de Temperatura",
    description="Converte entre Celsius e Fahrenheit",
)

iface.launch()