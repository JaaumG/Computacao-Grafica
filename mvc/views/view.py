import tkinter as tk
from tkinter import ttk, messagebox

class View:
    def __init__(self, root, controller):
        self.window = root
        self.controller = controller
        self.window.geometry("1000x750")
        self.window.title("Aplicação de Transformações 2D e Gerenciamento de Figuras")

        self.style = ttk.Style()
        self.style.configure('Cinza.TFrame', background='#4F4F4F')
        self.style.configure('BrancoTexto.TLabel', background='#4F4F4F', foreground='white')

        self._criar_frame_topo()
        self._criar_frame_principal()
        self._criar_frame_transformacoes()
        self._criar_frame_gerenciamento_figuras()

        self.draw_canvas = tk.Canvas(self.main_frame, bg="lightgray", width=500, height=400, borderwidth=2, relief="groove")
        self.draw_canvas.pack(pady=10)
        self.draw_canvas.bind("<Button-1>", self.on_canvas_click)

        self.update_figure_listbox([])

    def _criar_frame_topo(self):
        self.top_frame = ttk.Frame(self.window, height=50, style='Cinza.TFrame')
        self.top_frame.pack(fill="x", padx=1, pady=1)
        self.top_frame.pack_propagate(False)

        self.title_label = ttk.Label(self.top_frame,text="Desenhe sua figura, transforme e salve!",font=("Helvetica", 16, "bold"),style='BrancoTexto.TLabel')
        self.title_label.place(x=20, y=10)

    def _criar_frame_principal(self):
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(padx=1, pady=1, fill="both", expand=True)

    def _criar_frame_transformacoes(self):
        self.transform_frame = ttk.LabelFrame(self.main_frame, text="Transformações 2D")
        self.transform_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.transform_frame, text="Translação (dx, dy):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.entry_dx = ttk.Entry(self.transform_frame, width=10)
        self.entry_dx.grid(row=0, column=1, padx=5, pady=2)
        self.entry_dy = ttk.Entry(self.transform_frame, width=10)
        self.entry_dy.grid(row=0, column=2, padx=5, pady=2)
        ttk.Button(self.transform_frame, text="Aplicar Translação", command=self.controller.apply_translation).grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(self.transform_frame, text="Rotação (ângulo, px, py):").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.entry_angle = ttk.Entry(self.transform_frame, width=10)
        self.entry_angle.grid(row=1, column=1, padx=5, pady=2)
        self.entry_pivot_x_rot = ttk.Entry(self.transform_frame, width=10)
        self.entry_pivot_x_rot.grid(row=1, column=2, padx=5, pady=2)
        self.entry_pivot_y_rot = ttk.Entry(self.transform_frame, width=10)
        self.entry_pivot_y_rot.grid(row=1, column=3, padx=5, pady=2)
        ttk.Button(self.transform_frame, text="Aplicar Rotação", command=self.controller.apply_rotation).grid(row=1, column=4, padx=5, pady=2)

        ttk.Label(self.transform_frame, text="Escala (sx, sy, px, py):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.entry_sx = ttk.Entry(self.transform_frame, width=10)
        self.entry_sx.grid(row=2, column=1, padx=5, pady=2)
        self.entry_sy = ttk.Entry(self.transform_frame, width=10)
        self.entry_sy.grid(row=2, column=2, padx=5, pady=2)
        self.entry_pivot_x_scale = ttk.Entry(self.transform_frame, width=10)
        self.entry_pivot_x_scale.grid(row=2, column=3, padx=5, pady=2)
        self.entry_pivot_y_scale = ttk.Entry(self.transform_frame, width=10)
        self.entry_pivot_y_scale.grid(row=2, column=4, padx=5, pady=2)
        ttk.Button(self.transform_frame, text="Aplicar Escala", command=self.controller.apply_scale).grid(row=2, column=5, padx=5, pady=2)

        ttk.Button(self.transform_frame, text="Limpar Figura", command=self.controller.clear_figure).grid(row=3, column=0, columnspan=6, pady=5)

    def _criar_frame_gerenciamento_figuras(self):
        self.figure_management_frame = ttk.LabelFrame(self.main_frame, text="Gerenciamento de Figuras")
        self.figure_management_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.figure_management_frame, text="Nome da Figura:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.entry_figure_name = ttk.Entry(self.figure_management_frame, width=20)
        self.entry_figure_name.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        ttk.Button(self.figure_management_frame, text="Salvar Figura", command=self.controller.save_current_figure).grid(row=0, column=2, padx=5, pady=2)

        ttk.Label(self.figure_management_frame, text="Figuras Salvas:").grid(row=1, column=0, padx=5, pady=2, sticky="w")

        self.figure_listbox = tk.Listbox(self.figure_management_frame, height=5, width=30)
        self.figure_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="ew")
        self.figure_listbox.bind("<<ListboxSelect>>", self.on_figure_select)

        self.load_button = ttk.Button(self.figure_management_frame, text="Carregar Selecionada", command=self.controller.load_selected_figure)
        self.load_button.grid(row=2, column=2, padx=5, pady=2)
        self.load_button.config(state=tk.DISABLED)

        self.delete_button = ttk.Button(self.figure_management_frame, text="Excluir Selecionada", command=self.controller.delete_selected_figure)
        self.delete_button.grid(row=3, column=2, padx=5, pady=2)
        self.delete_button.config(state=tk.DISABLED)

    def _criar_frame_rodape(self):
        self.bottom_frame = ttk.Frame(self.window, height=0, style='Cinza.TFrame')
        self.bottom_frame.pack(fill="x", padx=1, pady=1, side="bottom")
        self.bottom_frame.pack_propagate(False)

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        self.controller.add_point_to_figure(x, y)

    def draw_figure(self, points):
        self.draw_canvas.delete("all")
        if not points:
            return

        for x, y in points:
            self.draw_canvas.create_oval(x-2, y-2, x+2, y+2, fill="blue", outline="blue")

        if len(points) > 1:
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i+1]
                self.draw_canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
            x1, y1 = points[-1]
            x2, y2 = points[0]
            self.draw_canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

    def get_translation_params(self):
        try:
            dx = float(self.entry_dx.get())
            dy = float(self.entry_dy.get())
            return dx, dy
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Translação: Por favor, insira números válidos para dx e dy.")
            return None, None

    def get_rotation_params(self):
        try:
            angle = float(self.entry_angle.get())
            cx = float(self.entry_pivot_x_rot.get() or self.draw_canvas.winfo_width()/2) # Default to canvas center
            cy = float(self.entry_pivot_y_rot.get() or self.draw_canvas.winfo_height()/2) # Default to canvas center
            return angle, cx, cy
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Rotação: Por favor, insira um ângulo e coordenadas de pivô válidas.")
            return None, None, None

    def get_scale_params(self):
        try:
            sx = float(self.entry_sx.get())
            sy = float(self.entry_sy.get())
            cx = float(self.entry_pivot_x_scale.get() or self.draw_canvas.winfo_width()/2) # Default to canvas center
            cy = float(self.entry_pivot_y_scale.get() or self.draw_canvas.winfo_height()/2) # Default to canvas center
            return sx, sy, cx, cy
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Escala: Por favor, insira fatores de escala e coordenadas de pivô válidas.")
            return None, None, None, None

    def get_figure_name_to_save(self):
        name = self.entry_figure_name.get().strip()
        if not name:
            messagebox.showwarning("Nome Vazio", "Por favor, insira um nome para a figura.")
            return None
        return name

    def get_selected_figure_name(self):
        selection_indices = self.figure_listbox.curselection()
        if selection_indices:
            return self.figure_listbox.get(selection_indices[0])
        else:
            messagebox.showwarning("Nenhuma Seleção", "Por favor, selecione uma figura da lista.")
            return None

    def update_figure_listbox(self, figure_names: list):
        self.figure_listbox.delete(0, tk.END)
        for name in figure_names:
            self.figure_listbox.insert(tk.END, name)
        self.load_button.config(state=tk.DISABLED)
        self.delete_button.config(state=tk.DISABLED)

    def on_figure_select(self, event):
        if self.figure_listbox.curselection():
            self.load_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.load_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def show_warning(self, title, message):
        messagebox.showwarning(title, message)