import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random  # Para generar el ID automáticamente
#from Cambiar_cliente_enprendedor import Cambiar

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

         # titulo_label =  tk.Label(frame, text="Informacion del cliente", fg=color_label, font=("arial", 14))
     #   titulo_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        # Campos para ingresar la información del cliente
        Id_label = tk.Label(frame, text="ID cliente", bg=color_frame, fg=color_label, font=("Arial", 12))
        Id_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.id_entry = tk.Entry(frame, font=("Arial", 14))
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        nombre_label = tk.Label(frame, text="Nombre:", bg=color_frame, fg=color_label, font=("Arial", 12))
        nombre_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.nombre_entry = tk.Entry(frame, font=("Arial", 14))
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        apellido_label = tk.Label(frame, text="Apellido:", bg=color_frame, fg=color_label, font=("Arial", 12))
        apellido_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.apellido_entry = tk.Entry(frame, font=("Arial", 14))
        self.apellido_entry.grid(row=1, column=1, padx=10, pady=5)

        # Atributo direccion
        direccion_label = tk.Label(frame, text="Dirección:", bg=color_frame, fg=color_label, font=("Arial", 12))
        direccion_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.direccion_entry = tk.Entry(frame, font=("Arial", 14))
        self.direccion_entry.grid(row=2, column=1, padx=10, pady=5)

        # Atributo regimen fiscal
        regimen_label = tk.Label(frame, text="Regimen Fiscal:", bg=color_frame, fg=color_label, font=("Arial", 12))
        regimen_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        # Opciones para el combobox (seleccionar el régimen fiscal)
        self.regimen_combobox = ttk.Combobox(frame, values=regimenes_fiscales, font=("Arial", 12))
        self.regimen_combobox.grid(row=3, column=1, padx=10, pady=5)

        # Botón para registrar el cliente
        register_button = tk.Button(frame, text="Registrar", command=self.register_client, bg=color_button,fg=color_button_text, font=("Arial", 14))
        register_button.grid(row=4, column=0, columnspan=2, pady=10)

        cambiarBoton = tk.Button(frame, text="Cambiar cliente a emprendedor", command=self.cambiarCliente, bg=color_button, fg=color_button_text)
        cambiarBoton.grid(row=5, column=0, columnspan=2, pady=10)

        # Configurar el tamaño de la ventana automáticamente
        frame.update_idletasks()
        window_width = frame.winfo_reqwidth() + 40  # Agregar 40 para dar espacio adicional
        window_height = frame.winfo_reqheight() + 40  # Agregar 40 para dar espacio adicional
        self.root.geometry(f"{window_width}x{window_height}")

    def generate_id(self):
        # Generar un ID cliente único (ejemplo: ID aleatorio de 4 dígitos)
        return str(random.randint(10000000, 9999999999))

    def register_client(self):
        # Generar un ID único para el cliente
        id = self.generate_id()

        # Obtener los valores ingresados por el usuario
        direccion = self.direccion_entry.get()
        regimen = self.regimen_combobox.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()

        # Guardar la información del cliente en un archivo de texto (o en tu base de datos)
        with open("clientes.txt", "a") as file:
            file.write(f"ID Cliente: {id}\n")
            file.write(f"Direccion: {direccion}\n")
            file.write(f"Regimen Fiscal: {regimen}\n")
            file.write(f"Nombre: {nombre}\n")
            file.write(f"Apellido: {apellido}\n\n")

        # Mostrar un mensaje de confirmación
        message = f"Cliente registrado:\nID Cliente: {id}\nNombre: {nombre}\nApellido: {apellido}"
        messagebox.showinfo("Registro Exitoso", message)

        ventanaCambiar = Cambiar(self.root, self.id_entry.get(), self.nombre_entry.get(), self.apellido_entry.get(), self.direccion_entry.get(), self.regimen_combobox.get())
        ventanaCambiar.show_info(id, nombre, apellido, direccion, regimen)
        #ventanaCambiar.show_info()
        # Cerrar la ventana de registro de cliente
        self.root.destroy()
    
    def cambiarCliente(self):
        ventanaCambiar = tk.Toplevel(self.root)
        from Cambiar_cliente_enprendedor import Cambiar
        ventanaCambiar = Cambiar(self.root, self.id_entry.get(), self.nombre_entry.get(), self.apellido_entry.get(), self.direccion_entry.get(), self.regimen_combobox.get())
       # ventanaCambiar.show_info()
      #  ventanaCambiar.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AddClientApp(root)
   # ventanaCambiar = Cambiar(root)
    root.mainloop()
