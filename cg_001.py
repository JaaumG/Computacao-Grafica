import tkinter as tk

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Desenhando um Segmento de Reta")

        # Definir dimensões do canvas
        self.canvas_largura = 400
        self.canvas_altura = 400

        # Definir limites do mundo real para normalização
        self.x_mundo_min = 0
        self.x_mundo_max = 10
        self.y_mundo_min = 0
        self.y_mundo_max = 10

        # Criar Canvas para desenhar
        self.canvas = tk.Canvas(self.root, width=self.canvas_largura, height=self.canvas_altura, bg="white")
        self.canvas.pack()

        # Botão para desenhar
        self.botao = tk.Button(self.root, text="Desenhar Reta", command=self.desenhar_reta)
        self.botao = tk.Button(self.root, text="Desenhar Triângulo", command=self.desenhar_triangulo)
        self.botao.pack()

    def desenhar_triangulo(self):
        # Definir as coordenadas do triângulo no mundo real
        x1_mundo, y1_mundo = 2, 2
        x2_mundo, y2_mundo = 8, 2
        x3_mundo, y3_mundo = 5, 8

        # Normalizar coordenadas para o espaço do canvas
        x1_canvas = self.normalizar_x(x1_mundo)
        y1_canvas = self.normalizar_y(y1_mundo)
        x2_canvas = self.normalizar_x(x2_mundo)
        y2_canvas = self.normalizar_y(y2_mundo)
        x3_canvas = self.normalizar_x(x3_mundo)
        y3_canvas = self.normalizar_y(y3_mundo)

        # Desenhar o triângulo no canvas
        self.canvas.create_line(x1_canvas, y1_canvas, x2_canvas, y2_canvas, fill="red", width=2)
        self.canvas.create_line(x2_canvas, y2_canvas, x3_canvas, y3_canvas, fill="red", width=2)
        self.canvas.create_line(x3_canvas, y3_canvas, x1_canvas, y1_canvas, fill="red", width=2)

    def desenhar_reta(self):
        # Definir as coordenadas do segmento de reta no mundo real
        x1_mundo, y1_mundo = 2, 2  # Ponto inicial no mundo real
        x2_mundo, y2_mundo = 8, 8  # Ponto final no mundo real

        # Normalizar coordenadas para o espaço do canvas
        x1_canvas = self.normalizar_x(x1_mundo)
        y1_canvas = self.normalizar_y(y1_mundo)
        x2_canvas = self.normalizar_x(x2_mundo)
        y2_canvas = self.normalizar_y(y2_mundo)

        # Desenhar o segmento de reta no canvas
        self.canvas.create_line(x1_canvas, y1_canvas, x2_canvas, y2_canvas, fill="blue", width=2)

    def normalizar_x(self, x_mundo):
        return (x_mundo - self.x_mundo_min) / (self.x_mundo_max - self.x_mundo_min) * (self.canvas_largura - 1)

    def normalizar_y(self, y_mundo):
        return (1 - (y_mundo - self.y_mundo_min) / (self.y_mundo_max - self.y_mundo_min)) * (self.canvas_altura - 1)

# Criar a janela principal
root = tk.Tk()
app = InterfaceGrafica(root)
root.mainloop()
