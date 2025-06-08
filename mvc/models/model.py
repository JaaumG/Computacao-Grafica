import sqlite3
import numpy as np
import json

class Model:
    def __init__(self):
        self.db_connection = sqlite3.connect('figures.db')
        cursor = self.db_connection.cursor()

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS figures (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL UNIQUE,
                            points TEXT NOT NULL
                       )
                       ''')
        self.db_connection.commit()

        self.points = []

    def add_point(self, x: float, y: float):
        self.points.append([x, y, 1])
        return self.points

    def clear_points(self):
        self.points = []
        return self.points

    def get_points(self):
        return [[p[0], p[1]] for p in self.points]

    def set_points(self, points_2d: list):
        self.points = [[p[0], p[1], 1] for p in points_2d]

    def apply_transformation(self, matrix: np.array):
        if not self.points:
            return None

        transformed_points = []
        for point in self.points:
            p_vector = np.array(point).reshape(3, 1)
            transformed_p = np.dot(matrix, p_vector)
            transformed_points.append(transformed_p.flatten().tolist())
        self.points = transformed_points
        return self.points

    def translate(self, dx: float, dy: float):
        translation_matrix = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ])
        self.apply_transformation(translation_matrix)

    def rotate(self, angle_degrees: float, cx: float = 0, cy: float = 0):
        angle_radians = np.radians(angle_degrees)
        cos_theta = np.cos(angle_radians)
        sin_theta = np.sin(angle_radians)

        translate_to_origin = np.array([
            [1, 0, -cx],
            [0, 1, -cy],
            [0, 0, 1]
        ])
        rotate_matrix = np.array([
            [cos_theta, -sin_theta, 0],
            [sin_theta, cos_theta, 0],
            [0, 0, 1]
        ])
        translate_back = np.array([
            [1, 0, cx],
            [0, 1, cy],
            [0, 0, 1]
        ])

        transformation_matrix = np.dot(translate_back, np.dot(rotate_matrix, translate_to_origin))
        self.apply_transformation(transformation_matrix)

    def scale(self, sx: float, sy: float, cx: float = 0, cy: float = 0):
        translate_to_origin = np.array([
            [1, 0, -cx],
            [0, 1, -cy],
            [0, 0, 1]
        ])
        scale_matrix = np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ])
        translate_back = np.array([
            [1, 0, cx],
            [0, 1, cy],
            [0, 0, 1]
        ])

        transformation_matrix = np.dot(translate_back, np.dot(scale_matrix, translate_to_origin))
        self.apply_transformation(transformation_matrix)

    def save_figure(self, figure_name: str) -> bool:
        if not self.points:
            print("Model: Nenhuma figura para salvar.")
            return False

        points_to_save = [[p[0], p[1]] for p in self.points]
        points_json = json.dumps(points_to_save)

        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''
                           INSERT INTO figures (name, points)
                           VALUES (?, ?)
                           ''', (figure_name, points_json))
            self.db_connection.commit()
            print(f"Model: Figura '{figure_name}' salva com sucesso!")
            return True
        except sqlite3.IntegrityError:
            print(f"Model: Erro: Figura com o nome '{figure_name}' já existe.")
            return False
        except sqlite3.Error as e:
            print(f"Model: Erro ao salvar figura: {e}")
            return False

    def load_figure(self, figure_name: str):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('SELECT points FROM figures WHERE name = ?', (figure_name,))
            result = cursor.fetchone()
            if result:
                points_json = result[0]
                loaded_points_2d = json.loads(points_json)
                self.set_points(loaded_points_2d)
                print(f"Model: Figura '{figure_name}' carregada com sucesso!")
                return self.get_points()
            else:
                print(f"Model: Figura com o nome '{figure_name}' não encontrada.")
                return []
        except sqlite3.Error as e:
            print(f"Model: Erro ao carregar figura: {e}")
            return []

    def get_all_figure_names(self) -> list:
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('SELECT name FROM figures ORDER BY name')
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Model: Erro ao listar nomes de figuras: {e}")
            return []