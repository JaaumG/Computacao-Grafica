import tkinter as tk

class AplicativoReta:
    def __init__(self):
        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("Segmento de Reta com Coordenadas Normalizadas")

        # Definir dimensões do canvas
        self.largura_canvas = 400
        self.altura_canvas = 300

        # Definir limites do mundo (sistema de coordenadas do usuário)
        self.x_min_mundo = -10
        self.x_max_mundo = 10
        self.y_min_mundo = -10
        self.y_max_mundo = 10

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
                               text="Desenhar Reta",
                               command=self.desenhar_reta)
        self.botao.pack()

    def mapear_x(self, x_mundo):
        # Mapeia a coordenada x do mundo para a coordenada x do dispositivo
        return self.largura_canvas * (x_mundo - self.x_min_mundo) / (self.x_max_mundo - self.x_min_mundo)

    def mapear_y(self, y_mundo):
        # Mapeia a coordenada y do mundo para a coordenada y do dispositivo
        # Note a inversão do Y para que o 0 fique na parte inferior
        return self.altura_canvas * (1 - (y_mundo - self.y_min_mundo) / (self.y_max_mundo - self.y_min_mundo))

    def desenhar_reta(self):
        # Pontos no sistema de coordenadas do mundo
        x1_mundo, y1_mundo = -5, -5  # Ponto inicial no mundo
        x2_mundo, y2_mundo = 5, 5    # Ponto final no mundo

        # Converter para coordenadas do dispositivo
        x1_dispositivo = self.mapear_x(x1_mundo)
        y1_dispositivo = self.mapear_y(y1_mundo)
        x2_dispositivo = self.mapear_x(x2_mundo)
        y2_dispositivo = self.mapear_y(y2_mundo)

        # Desenhar a reta usando as coordenadas do dispositivo
        self.canvas.create_line(x1_dispositivo, y1_dispositivo,
                                x2_dispositivo, y2_dispositivo,
                                fill="blue", width=2)

    def executar(self):
        # Iniciar o loop principal da aplicação
        self.janela.mainloop()

# Criar e executar a aplicação
if __name__ == "__main__":
    app = AplicativoReta()
    app.executar()