import tkinter as tk

# 1 Criar uma janela
window = tk.Tk()
window.geometry("400x400")  # Largura x Altura
window.title("Primeira Janela")  # Titulo da janela

# 2 - adiocionar um frame
frame = tk.Frame(window, width=400, height=400)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - adicionando um label
label = tk.Label(frame, text="Ola, Mundo!")
label.pack(fill='x', expand=True)


# 4 - adicionar o input text
frase_lab = tk.Label(frame, text="Digite uma frase:")
frase_lab.pack(fill='x', expand=True)

frase_input = tk.Entry(frame)
frase_input.pack(fill='x', expand=True)


# 5 Funcao do botao
def click():
    label.config(text=frase_input.get())


# 6 - Adicionar um botao
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()  # Executar a janela
