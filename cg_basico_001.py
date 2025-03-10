import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Segmento de Reta Simples")

# Criar um canvas (área de desenho)
canvas = tk.Canvas(janela, width=400, height=300, bg="white")
canvas.pack()

# Desenhar uma linha reta
# create_line(x1, y1, x2, y2) - onde (x1,y1) é o ponto inicial e (x2,y2) é o ponto final
canvas.create_line(50, 50, 350, 250, fill="blue", width=2)

# Iniciar o loop principal da aplicação
janela.mainloop()
