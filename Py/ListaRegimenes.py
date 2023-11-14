import tkinter as tk
from tkinter import ttk, Text, END, messagebox , Label
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk, Image

class Listaregimenes:
    def __init__(self, root): 
        self.root = root
        self.root.title("Lista de Emprendedores")

        # Obtiene el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana en la pantalla
        window_width = 400
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Establece la geometría de la ventana

        # Colores personalizados de la paleta
        color_frame = "#009688"  # VERDE PRIMARIO
        color_label = "#FFFFFF"  # BLANCO
        color_button = "#607D8B"  # GRIS OSCURO
        color_button_text = "#000000"  # BLANCO

        # Crear un marco principal para organizar los elementos de la interfaz
        frame = tk.Frame(root, bg=color_frame, bd=5)
        frame.grid(row=0, column=0, sticky="nsew")
        
        imagenImportada = Image.open("LogoB.png")
        imagenRedimensionada = imagenImportada.resize((128,64), Image.BILINEAR)
        imagen_Logo = ImageTk.PhotoImage(imagenRedimensionada)
        
        etiqueta_logo = Label(frame, image= imagen_Logo, bg='WHITE')
        etiqueta_logo.noMeBorresCrack = imagen_Logo
        etiqueta_logo.grid(row=0, column=0, padx=10, pady=10)

        # Etiqueta de título
        title_label = tk.Label(frame, text="Lista de regimenes", font=("Helvetica", 20), bg=color_frame,
                               fg=color_label)
        title_label.grid(row=1, column=0, columnspan=2, pady=(20, 30))

        # Widget de texto para mostrar la lista de emprendedores
        self.regimenes_text = Text(frame, bg=color_frame, fg=color_button_text)
        self.regimenes_text.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Botón para cargar la lista de emprendedores
        regimenes_button = ttk.Button(frame, text="Cargar Regimenes", command=self.cargarRegimenes, style="Custom.TButton")
        regimenes_button.grid(row=3, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

        # Cargar el estilo personalizado para los botones
        s = ttk.Style()
        s.configure("Custom.TButton", background=color_button, foreground=color_button_text)

        # Configurar la expansión de las filas y columnas
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        # Calcular el tamaño necesario para la ventana basado en el contenido
        frame.update_idletasks()
        window_width = frame.winfo_width() + 10  # Agregar un poco de espacio
        window_height = frame.winfo_height() + 10

        # Obtener el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana en la pantalla
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Configurar la geometría de la ventana
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")


    def cargarRegimenes(self):
        messagebox.showinfo(title="lsita de regimenes", message="lista")





if __name__ == "__main__":
    root = tk.Tk()
    app = Listaregimenes(root)
    root.mainloop()
