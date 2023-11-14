import tkinter as tk
from tkinter import ttk
from ModCliente import (ModifyClientInfoWindow)
from ModificarEmprendedor import (ModificarEmprendedor)
from PIL import ImageTk, Image

# Clase para la ventana principal
class ModifyInfoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Modificar Información")

        # Tamaño de la ventana principal
        window_width = 400
        window_height = 200

        # Obtener el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana principal en la pantalla
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Colores personalizados de la paleta
        color_frame = "#009688"  # VERDE PRIMARIO
        color_label = "#FFFFFF"  # BLANCO
        color_button = "#607D8B"  # GRIS OSCURO
        color_button_text = "#FFFFFF"  # BLANCO

        # Configurar el fondo de la ventana principal con el color deseado
        self.root.configure(bg=color_frame)

        # Crear un marco principal para organizar los elementos de la interfaz principal
        frame = tk.Frame(root, bg=color_frame, bd=5)
        frame.pack(fill="both", expand=True)

        # Etiqueta para el título de la ventana principal
        title_label = ttk.Label(frame, text="Modificar Información", background=color_frame, foreground=color_label,
                                font=("Helvetica", 16), anchor="center", justify="center")
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Botón para modificar la información del cliente
        client_button = ttk.Button(frame, text="Modificar Información de Cliente",
                                   command=self.modify_client_info, style="TButton")
        client_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        emprendedor_boton = ttk.Button(frame, text="Modificar Informacion del emprendedor", command=self.modificar_emprededor_info, style="TButton")
        emprendedor_boton.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def modify_client_info(self):
        # Abre la ventana de modificación de información del cliente
        client_info_window = tk.Toplevel(self.root)
        ModifyClientInfoWindow(client_info_window)
        client_info_window.transient(self.root)
        client_info_window.grab_set()
        client_info_window.wait_window()

    def modificar_emprededor_info(self):
        emprendedor_window = tk.Toplevel(self.root)
        ModificarEmprendedor(emprendedor_window)
        emprendedor_window.transient(self.root)
        emprendedor_window.grab_set()
        emprendedor_window.wait_window()


if __name__ == "__main__":
    root = tk.Tk()
    app = ModifyInfoWindow(root)
    root.mainloop()
