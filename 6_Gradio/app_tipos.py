import gradio as gr


def processar_dados(texto, numero, imagem, lista_texto, cor, opcoes):
    texto_revertido = texto[::-1]
    dobro_numero = numero * 2
    msg_imgaem = "Imagem carregada com sucesso!" if imagem else "Imagem nao carregada"
    lista_processada = (
        [[item] for item in lista_texto.splitlines()] if lista_texto else []
    )

    return (
        texto_revertido,
        dobro_numero,
        msg_imgaem,
        lista_processada,
        f"Cor selecionada: {cor}",
        opcoes,
    )


iface = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(label="Texto"),
        gr.Slider(minimum=0, maximum=100, step=1, label="Numero", value=0),
        gr.Image(type="pil", label="Imagem"),
        gr.Textbox(
            label="Lista de Texto", lines=4, placeholder="Digite uma lista de texto"
        ),
        gr.ColorPicker(label="Selecione uma cor"),
        gr.CheckboxGroup(["Opção 1", "Opção 2", "Opção 3"]),
    ],
    outputs=[
        gr.Textbox(label="Texto Revertido"),
        gr.Number(label="Dobro do Numero"),
        gr.Textbox(label="Mensagem da Imagem"),
        gr.Dataframe(label="Lista Processada"),
        gr.Textbox(label="Cor Selecionada"),
        gr.Textbox(label="Opcoes Selecionadas"),
    ],
    title="Processador de Dados",
    description="Exemplo de processamento de dados com Gradio",
)
iface.launch()
