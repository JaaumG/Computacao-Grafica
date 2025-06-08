from views.view import View
from models.model import Model
import tkinter as tk
from tkinter import messagebox # Import messagebox

class Controller:
    def __init__(self, model, root):
        self.model = model
        self.view = View(root, self)
        self.view.draw_figure(self.model.get_points())
        self.view.update_figure_listbox(self.model.get_all_figure_names())

    def add_point_to_figure(self, x: int, y: int):
        self.model.add_point(x, y)
        self.view.draw_figure(self.model.get_points())
        print(f"Ponto adicionado: ({x}, {y})")

    def clear_figure(self):
        self.model.clear_points()
        self.view.draw_figure(self.model.get_points())
        self.view.show_info("Limpar Figura", "A figura atual foi limpa.")
        print("Figura limpa.")

    def apply_translation(self):
        dx, dy = self.view.get_translation_params()
        if dx is not None and dy is not None:
            self.model.translate(dx, dy)
            self.view.draw_figure(self.model.get_points())
            print(f"Translação aplicada: dx={dx}, dy={dy}")

    def apply_rotation(self):
        angle, cx, cy = self.view.get_rotation_params()
        if angle is not None and cx is not None and cy is not None:
            self.model.rotate(angle, cx, cy)
            self.view.draw_figure(self.model.get_points())
            print(f"Rotação aplicada: ângulo={angle}°, pivô=({cx}, {cy})")

    def apply_scale(self):
        sx, sy, cx, cy = self.view.get_scale_params()
        if sx is not None and sy is not None and cx is not None and cy is not None:
            self.model.scale(sx, sy, cx, cy)
            self.view.draw_figure(self.model.get_points())
            print(f"Escala aplicada: sx={sx}, sy={sy}, pivô=({cx}, {cy})")

    def save_current_figure(self):
        figure_name = self.view.get_figure_name_to_save()
        if figure_name:
            if self.model.save_figure(figure_name):
                self.view.show_info("Salvar Figura", f"Figura '{figure_name}' salva com sucesso!")
                self.view.update_figure_listbox(self.model.get_all_figure_names())
                self.view.entry_figure_name.delete(0, tk.END)
            else:
                self.view.show_error("Erro ao Salvar", f"Não foi possível salvar a figura '{figure_name}'. Talvez o nome já exista.")

    def load_selected_figure(self):
        figure_name = self.view.get_selected_figure_name()
        if figure_name:
            loaded_points = self.model.load_figure(figure_name)
            if loaded_points is not None:
                self.view.draw_figure(loaded_points)
                self.view.show_info("Carregar Figura", f"Figura '{figure_name}' carregada.")
            else:
                self.view.show_error("Erro ao Carregar", f"Não foi possível carregar a figura '{figure_name}'.")

    def delete_selected_figure(self):
        figure_name = self.view.get_selected_figure_name()
        if figure_name:
            if messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir a figura '{figure_name}'?"):
                try:
                    cursor = self.model.db_connection.cursor()
                    cursor.execute('DELETE FROM figures WHERE name = ?', (figure_name,))
                    self.model.db_connection.commit()
                    self.view.show_info("Excluir Figura", f"Figura '{figure_name}' excluída com sucesso!")
                    self.view.update_figure_listbox(self.model.get_all_figure_names())
                    self.model.clear_points() # Clear the current figure in memory as it was deleted
                    self.view.draw_figure([])
                except sqlite3.Error as e:
                    self.view.show_error("Erro ao Excluir", f"Erro ao excluir figura: {e}")