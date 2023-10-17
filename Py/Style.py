import tkinter as tk
from tkinter import ttk


def set_custom_style():
    style = ttk.Style()

    # Colores personalizados de la paleta
    color_frame = "#009688"  # VERDE PRIMARIO
    color_label = "#FFFFFF"  # BLANCO
    color_button = "#607D8B"  # GRIS OSCURO
    color_button_text = "#000000"  # BLANCO

    # Configurar el estilo para los botones
    style.configure("Custom.TButton",
                    background=color_button,
                    foreground=color_button_text)
