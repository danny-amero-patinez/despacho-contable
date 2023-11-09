import tkinter as tk
import random
from tkinter import ttk
from tkinter import messagebox


class principalAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla de Inicio")

        # Tamaño de la ventana
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
        color_button_text = "#FFFFFF"  # BLANCO

        # Configurar el fondo de la ventana principal con el color deseado
        self.root.configure(bg=color_frame)

        # Crear un marco principal para organizar los elementos de la interfaz
        frame = tk.Frame(root, bg=color_frame, bd=5)
        frame.grid(row=0, column=0, sticky="nsew")

        # Configurar las columnas y filas para hacer que la interfaz sea responsiva
        root.columnconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        # Etiqueta de título
        title_label = tk.Label(frame, text="Bienvenido", font=("Helvetica", 20), bg=color_frame, fg=color_label)
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 30))

        # Botones
        buttons_frame = ttk.LabelFrame(frame, text="", padding=10)
        buttons_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        # Botón para registrar un nuevo cliente
        register_client_button = ttk.Button(buttons_frame, text="Registrar Agentes")
        register_client_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para registrar un nuevo regimen
        registrar_regimen_boton = ttk.Button(buttons_frame, text="Agregar regimen fiscal", command=self.registrarRegimen)
        registrar_regimen_boton.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Botón para ver la lista de clientes
        view_clients_button = ttk.Button(buttons_frame, text="Ver Agentes")
        view_clients_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para ver la lista de regimenes
        regimen_boton = ttk.Button(buttons_frame, text="Ver regimenes fiscales", command=self.verRegimenes)
        regimen_boton.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Botón para modificar la información
        modify_info_button = ttk.Button(buttons_frame, text="Modificar Información de agentes")
        modify_info_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

        # Botón para cerrar la sesión
        logout_button = ttk.Button(buttons_frame, text="Cerrar Sesión", command=self.logout)
        logout_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

        # Configurar las columnas y filas para hacer que la interfaz sea responsiva
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)



    def logout(self):
        # Cerrar la ventana actual
        self.root.destroy()

        # Crear una nueva ventana de inicio de sesión
        login_window = tk.Tk()
        from Login import LoginApp
        app = LoginApp(login_window)

    def registrarRegimen(self):
      #  messagebox.showinfo(message="Se registro correctamente el regimen", title="registro")
        self.root.destroy()

        ventanaRegimen = tk.Tk()
        from RegimenesFiscales import RegimenesFiscales
        RegimenesFiscales(ventanaRegimen)              
        ventanaRegimen.mainloop()

    
    def verRegimenes(self):
        messagebox.showinfo(message="lista de clientes", title="Lista regimenes")
       # self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = principalAdmin(root)
    root.mainloop()

    # Centrar la ventana en la pantalla
    window_width = 400
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.mainloop()