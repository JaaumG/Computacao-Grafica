import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Segmento de Reta com Botão")

# Função que será chamada quando o botão for clicado
def desenhar_reta():
    canvas.create_line(50, 50, 350, 250, fill="blue", width=2)

# Criar um canvas (área de desenho)
canvas = tk.Canvas(janela, width=400, height=300, bg="white")
canvas.pack()

# Criar um botão
botao = tk.Button(janela, text="Desenhar Reta", command=desenhar_reta)
botao.pack()

# Iniciar o loop principal da aplicação
janela.mainloop()