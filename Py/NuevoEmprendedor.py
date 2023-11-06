import tkinter as tk
from tkinter import messagebox


class AddEntrepreneurApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Emprendedor")

        # Obtiene el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana en la pantalla
        window_width = 300
        window_height = 200
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Establece la geometría de la ventana

        # Colores personalizados de la paleta
        color_frame = "#009688"  # VERDE PRIMARIO
        color_label = "#FFFFFF"  # BLANCO
        color_button = "#607D8B"  # GRIS OSCURO
        color_button_text = "#000000"  # BLANCO

        # Configura el fondo de la ventana principal con el color deseado
        self.root.configure(bg=color_frame)

        # Crear un marco para organizar los elementos de la interfaz
        frame = tk.Frame(root, padx=20, pady=20, bg=color_frame)
        frame.pack(expand=True, fill="both")

        # Campos para ingresar la información del emprendedor
        name_label = tk.Label(frame, text="Nombre:", bg=color_frame, fg=color_label)
        name_label.grid(row=1, column=0, sticky="w")

        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        last_name_label = tk.Label(frame, text="Apellido:", bg=color_frame, fg=color_label)
        last_name_label.grid(row=2, column=0, sticky="w")

        self.last_name_entry = tk.Entry(frame)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Botón para registrar el emprendedor
        register_button = tk.Button(frame, text="Registrar", command=self.register_entrepreneur, bg=color_button,
                                    fg=color_button_text)
        register_button.grid(row=6, column=0, columnspan=2, pady=10)

    def register_entrepreneur(self):
        # Obtener los valores ingresados por el usuario
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()

        # Guardar la información del emprendedor en un archivo de texto
        with open("emprendedores.txt", "a") as file:
            file.write(f"Nombre: {name}\nApellido: {last_name}\n\n")

        # Mostrar un mensaje de confirmación
        message = f"Emprendedor registrado:\nNombre: {name}\nApellido: {last_name}"
        messagebox.showinfo("Registro Exitoso", message)

        # Cerrar la ventana de registro de emprendedores
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AddEntrepreneurApp(root)
    root.mainloop() 
