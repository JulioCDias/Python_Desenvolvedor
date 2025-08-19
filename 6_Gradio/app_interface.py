import gradio as gr


def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    estilo = (
        f"background-color: {cor_fundo}; "
        f"color: {cor_texto}; "
        f"font-size: {tamanho_fonte}px; "
        f"font-family: {estilo_fonte};"
    )
    return f'<p style="{estilo}">{texto}</p>'


iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite um texto"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
        gr.Slider(minimum=8, maximum=72, step=1, label="Tamanho da Fonte"),
        gr.Radio(
            choices=["Arial", "Times New Roman", "Verdana", "Courier New"],
            label="Estilo da Fonte",
        ),
    ],
    outputs=gr.HTML(label="Texto Personalizado"),
    title="Personalizador de Texto",
    description="Personalize o texto com cores, tamanhos e estilos",
)
iface.launch()
