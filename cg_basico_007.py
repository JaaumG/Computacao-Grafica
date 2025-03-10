import tkinter as tk

class AplicativoReta:
    def __init__(self):
        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("Triângulo com Coordenadas Normalizadas")

        # Definir dimensões do canvas
        self.largura_canvas = 400
        self.altura_canvas = 300

        # Definir limites do mundo
        self.x_min_mundo = -10
        self.x_max_mundo = 10
        self.y_min_mundo = -10
        self.y_max_mundo = 10

        # Definir os vértices do triângulo usando listas
        self.vertices = [
            [-5, -5],  # Vértice 1
            [5, -5],   # Vértice 2
            [0, 5]     # Vértice 3
        ]

        # Criar os componentes da interface
        self.criar_widgets()

    def criar_widgets(self):
        # Criar um canvas
        self.canvas = tk.Canvas(self.janela,
                                width=self.largura_canvas,
                                height=self.altura_canvas,
                                bg="white")
        self.canvas.pack()

        # Criar botões
        self.botao_desenhar = tk.Button(self.janela,
                                        text="Desenhar Triângulo",
                                        command=self.desenhar_triangulo)
        self.botao_desenhar.pack()

        self.botao_transladar = tk.Button(self.janela,
                                          text="Transladar para Direita",
                                          command=self.transladar_direita)
        self.botao_transladar.pack()

    def mapear_x(self, x_mundo):
        return self.largura_canvas * (x_mundo - self.x_min_mundo) / (self.x_max_mundo - self.x_min_mundo)

    def mapear_y(self, y_mundo):
        return self.altura_canvas * (1 - (y_mundo - self.y_min_mundo) / (self.y_max_mundo - self.y_min_mundo))

    def desenhar_segmento(self, x1_mundo, y1_mundo, x2_mundo, y2_mundo):
        x1_dispositivo = self.mapear_x(x1_mundo)
        y1_dispositivo = self.mapear_y(y1_mundo)
        x2_dispositivo = self.mapear_x(x2_mundo)
        y2_dispositivo = self.mapear_y(y2_mundo)

        self.canvas.create_line(x1_dispositivo, y1_dispositivo,
                                x2_dispositivo, y2_dispositivo,
                                fill="blue", width=2)

    def desenhar_triangulo(self):
        # Limpar o canvas antes de desenhar
        self.canvas.delete("all")

        # Desenhar os três lados do triângulo
        self.desenhar_segmento(self.vertices[0][0], self.vertices[0][1],
                               self.vertices[1][0], self.vertices[1][1])

        self.desenhar_segmento(self.vertices[1][0], self.vertices[1][1],
                               self.vertices[2][0], self.vertices[2][1])

        self.desenhar_segmento(self.vertices[2][0], self.vertices[2][1],
                               self.vertices[0][0], self.vertices[0][1])

    def transladar_direita(self):
        # Transladar 2 unidades para a direita
        for vertice in self.vertices:
            vertice[0] += 2  # Incrementa a coordenada x

        # Redesenhar o triângulo na nova posição
        self.desenhar_triangulo()

    def executar(self):
        self.janela.mainloop()

# Criar e executar a aplicação
if __name__ == "__main__":
    app = AplicativoReta()
    app.executar()