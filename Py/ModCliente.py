import tkinter as tk
from tkinter import ttk, messagebox


# Clase para la ventana de modificación de información del cliente
class ModifyClientInfoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Modificar Información del Cliente")
        self.editing = False  # Variable para rastrear si se está editando

        # Tamaño de la ventana de modificación de cliente
        window_width = 400
        window_height = 400

        # Obtener el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana en la pantalla
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Colores personalizados de la paleta
        color_frame = "#009688"  # VERDE PRIMARIO
        color_label = "#FFFFFF"  # BLANCO
        color_button = "#607D8B"  # GRIS OSCURO
        color_button_text = "#000000"  # BLANCO

        # Configurar el fondo de la ventana de modificación de cliente con el color deseado
        self.root.configure(bg=color_frame)

        # Crear un marco principal para organizar los elementos de la interfaz de modificación de cliente
        frame = tk.Frame(root, bg=color_frame, bd=5)
        frame.pack(fill="both", expand=True)

        # Etiqueta para el título de la ventana de modificación de cliente
        title_label = ttk.Label(frame, text="Modificar Información del Cliente", background=color_frame,
                                foreground=color_label, font=("Helvetica", 16), anchor="center", justify="center")
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta para seleccionar al cliente a modificar
        select_label = ttk.Label(frame, text="Selecciona al Cliente:", background=color_frame, foreground=color_label)
        select_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Lista desplegable para seleccionar al cliente
        self.client_names = []  # Lista para almacenar nombres de clientes
        self.selected_client = tk.StringVar()
        self.client_dropdown = ttk.Combobox(frame, textvariable=self.selected_client, values=self.client_names)
        self.client_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Botón para cargar la información del cliente seleccionado
        load_button = ttk.Button(frame, text="Cargar Información", command=self.load_client_info, style="TButton")
        load_button.grid(row=1, column=2, padx=10, pady=5)

        # Campos de entrada para editar la información del cliente
        name_label = ttk.Label(frame, text="Nombre:", background=color_frame, foreground=color_label)
        name_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.name_entry = ttk.Entry(frame)
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)

        last_name_label = ttk.Label(frame, text="Apellido:", background=color_frame, foreground=color_label)
        last_name_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.last_name_entry = ttk.Entry(frame)
        self.last_name_entry.grid(row=3, column=1, padx=10, pady=5)

        direccion_label = ttk.Label(frame, text="Dirección:", background=color_frame, foreground=color_label)
        direccion_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.direccion_entry = ttk.Entry(frame)
        self.direccion_entry.grid(row=4, column=1, padx=10, pady=5)

        regimen_label = ttk.Label(frame, text="Régimen Fiscal:", background=color_frame, foreground=color_label)
        regimen_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.regimen_entry = ttk.Entry(frame)
        self.regimen_entry.grid(row=5, column=1, padx=10, pady=5)

        # Botón para aplicar los cambios y guardar la información del cliente
        save_button = ttk.Button(frame, text="Guardar Cambios", command=self.save_client_info, style="TButton")
        save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Deshabilitar la edición de los campos por defecto
        self.toggle_editing()

    def toggle_editing(self):
        # Alternar entre modo de edición y vista
        state = tk.NORMAL if self.editing else tk.DISABLED
        self.name_entry.config(state=state)
        self.last_name_entry.config(state=state)
        self.direccion_entry.config(state=state)
        self.regimen_entry.config(state=state)

    def load_client_info(self):
        selected_client = self.selected_client.get()
        if selected_client:
            try:
                # Leer la información del cliente seleccionado desde el archivo clientes.txt
                with open("clientes.txt", "r") as file:
                    client_data = file.readlines()
                    for line in client_data:
                        # Cada línea del archivo debe contener: Nombre, Apellido, Dirección, Régimen Fiscal
                        name, last_name, direccion, regimen = line.strip().split(",")
                        if f"{name} {last_name}" == selected_client:
                            # Mostrar la información en los campos de entrada
                            self.name_entry.delete(0, tk.END)
                            self.name_entry.insert(0, name)
                            self.last_name_entry.delete(0, tk.END)
                            self.last_name_entry.insert(0, last_name)
                            self.direccion_entry.delete(0, tk.END)
                            self.direccion_entry.insert(0, direccion)
                            self.regimen_entry.delete(0, tk.END)
                            self.regimen_entry.insert(0, regimen)
                            break
            except FileNotFoundError:
                messagebox.showerror("Error", "El archivo clientes.txt no existe.")
        else:
            messagebox.showwarning("Advertencia", "Selecciona un cliente antes de cargar la información.")

    def save_client_info(self):
        # Agregar aquí la lógica para guardar los cambios en la información del cliente
        # en tu base de datos o sistema de almacenamiento
        tk.messagebox.showinfo("Guardar Cambios", "Cambios guardados exitosamente")
        self.toggle_editing()  # Deshabilitar la edición


if __name__ == "__main__":
    root = tk.Tk()
    app = ModifyClientInfoWindow(root)
    root.mainloop()
