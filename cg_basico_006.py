import tkinter as tk


class AplicativoReta:
    def __init__(self):
        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("Triângulo com Coordenadas Normalizadas")

        # Definir dimensões do canvas
        self.largura_canvas = 400
        self.altura_canvas = 300

        # Definir limites do mundo (sistema de coordenadas do usuário)
        self.x_min_mundo = -10
        self.x_max_mundo = 10
        self.y_min_mundo = -10
        self.y_max_mundo = 10

        # Definir os vértices do triângulo no mundo
        self.vertices = [
            [-5, -5],  # Vértice 1
            [5, -5],  # Vértice 2
            [0, 5]  # Vértice 3
        ]

        # Criar os componentes da interface
        self.criar_widgets()

    def criar_widgets(self):
        # Criar um canvas (área de desenho)
        self.canvas = tk.Canvas(self.janela,
                                width=self.largura_canvas,
                                height=self.altura_canvas,
                                bg="white")
        self.canvas.pack()

        # Criar um botão
        self.botao = tk.Button(self.janela,
                               text="Desenhar Triângulo",
                               command=self.desenhar_triangulo)
        self.botao.pack()

    def mapear_x(self, x_mundo):
        # Mapeia a coordenada x do mundo para a coordenada x do dispositivo
        return self.largura_canvas * (x_mundo - self.x_min_mundo) / (self.x_max_mundo - self.x_min_mundo)

    def mapear_y(self, y_mundo):
        # Mapeia a coordenada y do mundo para a coordenada y do dispositivo
        return self.altura_canvas * (1 - (y_mundo - self.y_min_mundo) / (self.y_max_mundo - self.y_min_mundo))

    def desenhar_segmento(self, x1_mundo, y1_mundo, x2_mundo, y2_mundo):
        # Converter para coordenadas do dispositivo
        x1_dispositivo = self.mapear_x(x1_mundo)
        y1_dispositivo = self.mapear_y(y1_mundo)
        x2_dispositivo = self.mapear_x(x2_mundo)
        y2_dispositivo = self.mapear_y(y2_mundo)

        # Desenhar a reta usando as coordenadas do dispositivo
        self.canvas.create_line(x1_dispositivo, y1_dispositivo,
                                x2_dispositivo, y2_dispositivo,
                                fill="blue", width=2)

    def desenhar_triangulo(self):
        # Desenhar os três lados do triângulo
        # Lado 1: do vértice 0 ao vértice 1
        self.desenhar_segmento(self.vertices[0][0], self.vertices[0][1],
                               self.vertices[1][0], self.vertices[1][1])

        # Lado 2: do vértice 1 ao vértice 2
        self.desenhar_segmento(self.vertices[1][0], self.vertices[1][1],
                               self.vertices[2][0], self.vertices[2][1])

        # Lado 3: do vértice 2 ao vértice 0 (fechando o triângulo)
        self.desenhar_segmento(self.vertices[2][0], self.vertices[2][1],
                               self.vertices[0][0], self.vertices[0][1])

    def executar(self):
        # Iniciar o loop principal da aplicação
        self.janela.mainloop()


# Criar e executar a aplicação
if __name__ == "__main__":
    app = AplicativoReta()
    app.executar()
