import tkinter as tk
from tkinter import messagebox, ttk
import random  # Para generar el ID automáticamente

# Lista de regímenes fiscales en México
regimenes_fiscales = ["Régimen General de Ley", "Régimen de Incorporación Fiscal (RIF)",
                      "Régimen de Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras",
                      "Régimen de Arrendamiento", "Régimen de Sueldos y Salarios",
                      "Régimen de Personas Morales con Fines No Lucrativos",
                      "Régimen de Consolidación Fiscal", "Régimen de Actividades Empresariales y Profesionales",
                      "Régimen de Intereses", "Régimen de Dividendos"]


class AddClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Cliente")

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
        frame = tk.Frame(root, padx=20, pady=20, bg=color_frame)
        frame.pack(expand=True, fill="both")

        # Campos para ingresar la información del cliente
        name_label = tk.Label(frame, text="Nombre:", bg=color_frame, fg=color_label, font=("Arial", 14))
        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.name_entry = tk.Entry(frame, font=("Arial", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        last_name_label = tk.Label(frame, text="Apellido:", bg=color_frame, fg=color_label, font=("Arial", 14))
        last_name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.last_name_entry = tk.Entry(frame, font=("Arial", 14))
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Atributo direccion
        direccion_label = tk.Label(frame, text="Dirección:", bg=color_frame, fg=color_label, font=("Arial", 14))
        direccion_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.direccion_entry = tk.Entry(frame, font=("Arial", 14))
        self.direccion_entry.grid(row=2, column=1, padx=10, pady=5)

        # Atributo regimen fiscal
        regimen_fiscal_label = tk.Label(frame, text="Regimen Fiscal:", bg=color_frame, fg=color_label,
                                        font=("Arial", 14))
        regimen_fiscal_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        # Opciones para el combobox (seleccionar el régimen fiscal)
        self.regimen_fiscal_combobox = ttk.Combobox(frame, values=regimenes_fiscales, font=("Arial", 14))
        self.regimen_fiscal_combobox.grid(row=3, column=1, padx=10, pady=5)

        # Botón para registrar el cliente
        register_button = tk.Button(frame, text="Registrar", command=self.register_client, bg=color_button,
                                    fg=color_button_text, font=("Arial", 14))
        register_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Configurar el tamaño de la ventana automáticamente
        frame.update_idletasks()
        window_width = frame.winfo_reqwidth() + 40  # Agregar 40 para dar espacio adicional
        window_height = frame.winfo_reqheight() + 40  # Agregar 40 para dar espacio adicional
        self.root.geometry(f"{window_width}x{window_height}")

    def generate_id(self):
        # Generar un ID cliente único (ejemplo: ID aleatorio de 4 dígitos)
        return str(random.randint(10000000, 99999999))

    def register_client(self):
        # Generar un ID único para el cliente
        id_cliente = self.generate_id()

        # Obtener los valores ingresados por el usuario
        direccion = self.direccion_entry.get()
        regimen_fiscal = self.regimen_fiscal_combobox.get()
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()

        # Guardar la información del cliente en un archivo de texto (o en tu base de datos)
        with open("clientes.txt", "a") as file:
            file.write(f"ID Cliente: {id_cliente}\n")
            file.write(f"Dirección: {direccion}\n")
            file.write(f"Regimen Fiscal: {regimen_fiscal}\n")
            file.write(f"Nombre: {name}\n")
            file.write(f"Apellido: {last_name}\n\n")

        # Mostrar un mensaje de confirmación
        message = f"Cliente registrado:\nID Cliente: {id_cliente}\nNombre: {name}\nApellido: {last_name}"
        messagebox.showinfo("Registro Exitoso", message)

        # Cerrar la ventana de registro de cliente
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AddClientApp(root)
    root.mainloop()
