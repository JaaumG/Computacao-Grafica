import tkinter as tk

class AplicativoReta:
    def __init__(self):
        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("Segmento de Reta com Botão - POO")

        # Criar os componentes da interface
        self.criar_widgets()

    def criar_widgets(self):
        # Criar um canvas (área de desenho)
        self.canvas = tk.Canvas(self.janela, width=400, height=300, bg="white")
        self.canvas.pack()

        # Criar um botão
        self.botao = tk.Button(self.janela,
                               text="Desenhar Reta",
                               command=self.desenhar_reta)
        self.botao.pack()

    def desenhar_reta(self):
        # Método para desenhar a reta no canvas
        self.canvas.create_line(50, 50, 350, 250, fill="blue", width=2)

    def executar(self):
        # Iniciar o loop principal da aplicação
        self.janela.mainloop()

# Criar e executar a aplicação
if __name__ == "__main__":
    app = AplicativoReta()
    app.executar()