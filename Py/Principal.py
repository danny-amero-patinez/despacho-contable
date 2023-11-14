import tkinter as tk
from tkinter import ttk, Label, messagebox

from NuevoCliente import AddClientApp
from NuevoEmprendedor import AddEntrepreneur
from PIL import ImageTk, Image

class HomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla de Inicio")

        # Tamaño de la ventana
        window_width = 400
        window_height = 550

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

        imagenImportada = Image.open("Logo1.png")
        imagenRedimensionada = imagenImportada.resize((120, 120), Image.BILINEAR)
        imagen_Logo = ImageTk.PhotoImage(imagenRedimensionada)
        # Etiqueta contenedora de Logo
        etiqueta_logo = Label(frame, image=imagen_Logo, bg='WHITE')
        etiqueta_logo.noMeBorresCrack = imagen_Logo
        etiqueta_logo.grid(row=0, column=0, padx=0, pady=10)

        # Etiqueta de título
        title_label = tk.Label(frame, text="Bienvenido", font=("Helvetica", 20), bg=color_frame, fg=color_label)
        title_label.grid(row=1, column=0, columnspan=2, pady=(20, 30))

        # Botones
        buttons_frame = ttk.LabelFrame(frame, text="", padding=10)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        # Botón para registrar un nuevo cliente
        register_client_button = ttk.Button(buttons_frame, text="Registrar Cliente",
                                            command=self.open_client_registration)
        register_client_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para registrar un nuevo emprendedor
        register_entrepreneur_button = ttk.Button(buttons_frame, text="Registrar Emprendedor",
                                                  command=self.open_entrepreneur_registration)
        register_entrepreneur_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Botón para ver la lista de clientes
        view_clients_button = ttk.Button(buttons_frame, text="Ver Clientes", command=self.view_clients)
        view_clients_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para ver la lista de emprendedores
        view_entrepreneurs_button = ttk.Button(buttons_frame, text="Ver Emprendedores", command=self.view_entrepreneurs)
        view_entrepreneurs_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        cambiar_button = ttk.Button(buttons_frame, text="Cambiar cliente a emprendedor", command=self.cambiarClienteEmprendedor)
        cambiar_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

        # Botón para modificar la información
        modify_info_button = ttk.Button(buttons_frame, text="Modificar Información", command=self.modify_info)
        modify_info_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

        # Botón para cerrar la sesión
        logout_button = ttk.Button(buttons_frame, text="Cerrar Sesión", command=self.logout)
        logout_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

        # Configurar las columnas y filas para hacer que la interfaz sea responsiva
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)

    def open_client_registration(self):
        # Crear una nueva ventana para el registro de clientes
        client_registration_window = tk.Toplevel(self.root)
        app = AddClientApp(client_registration_window)

    def open_entrepreneur_registration(self):
        # Crear una nueva ventana para el registro de emprendedores
        entrepreneur_registration_window = tk.Toplevel(self.root)
        app = AddEntrepreneur(entrepreneur_registration_window)

    def view_clients(self):
        # Crear una nueva ventana para mostrar la lista de clientes
        client_list_window = tk.Toplevel(self.root)
        from ListaClientes import ClientListApp
        app = ClientListApp(client_list_window)

    def view_entrepreneurs(self):
        # Crear una nueva ventana para mostrar la lista de emprendedores
        entrepreneurs_window = tk.Toplevel(self.root)
        from ListaEmprendedores import EntrepreneurListApp
        app = EntrepreneurListApp(entrepreneurs_window)  # Usa la nueva clase

    def cambiarClienteEmprendedor(self):
        cambiar_window = tk.Toplevel(self.root)
        from Cliente import ClienteApp
        app = ClienteApp(cambiar_window)

    def modify_info(self):
        # Crear una nueva ventana para modificar la información
        modify_info_window = tk.Toplevel(self.root)
        from Modificar import ModifyInfoWindow
        app = ModifyInfoWindow(modify_info_window)

    def logout(self):
        # Cerrar la ventana actual
        self.root.destroy()

        # Crear una nueva ventana de inicio de sesión
        login_window = tk.Tk()
        from Login import LoginApp
        app = LoginApp(login_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = HomeApp(root)
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
