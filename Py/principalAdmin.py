import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from NuevoAgente import AgenteApp
from RegimenesFiscales import RegimenesFiscales
from ListaRegimenes import Listaregimenes
from ListaAgentes import AgentListApp
from ModificarAgente import ModificarAgenteApp
from Login import LoginApp


class PrincipalAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla de Inicio")

        window_width = 400
        window_height = 400

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        color_frame = "#009688"
        color_label = "#FFFFFF"
        color_button = "#607D8B"
        color_button_text = "#FFFFFF"

        self.root.configure(bg=color_frame)

        frame = tk.Frame(root, bg=color_frame, bd=5)
        frame.grid(row=0, column=0, sticky="nsew")

        root.columnconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        title_label = tk.Label(frame, text="Bienvenido", font=("Helvetica", 20), bg=color_frame, fg=color_label)
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 30))

        buttons_frame = ttk.LabelFrame(frame, text="", padding=10)
        buttons_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        register_client_button = ttk.Button(buttons_frame, text="Registrar Agentes", command=self.open_registrar_agente)
        register_client_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        registrar_regimen_boton = ttk.Button(buttons_frame, text="Agregar regimen fiscal",
                                             command=self.open_registrar_regimen)
        registrar_regimen_boton.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        view_clients_button = ttk.Button(buttons_frame, text="Ver Agentes", command=self.open_agent_list)
        view_clients_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        regimen_boton = ttk.Button(buttons_frame, text="Ver regimenes fiscales", command=self.ver_regimenes)
        regimen_boton.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        modify_info_button = ttk.Button(buttons_frame, text="Modificar Información de agentes", command=self.open_modificar_agente)
        modify_info_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

        logout_button = ttk.Button(buttons_frame, text="Cerrar Sesión", command=self.logout)
        logout_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)

        # Configurar el evento de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def logout(self):
        self.root.destroy()
        login_window = tk.Tk()
        app = LoginApp(login_window)

    def on_closing(self):
        # Mostrar un mensaje de advertencia antes de cerrar la ventana
        if messagebox.askokcancel("Cerrar la aplicación", "¿Está seguro de que desea cerrar la aplicación?"):
            self.root.destroy()

    def ver_regimenes(self):
        lista_regimenes_window = tk.Toplevel(self.root)
        app = Listaregimenes(lista_regimenes_window)
      #  messagebox.showinfo(message="lista de clientes", title="Lista regimenes")

    def open_registrar_agente(self):
        # Crear una nueva ventana para el registro de agentes
        nuevo_agente_window = tk.Toplevel(self.root)
        app = AgenteApp(nuevo_agente_window)

    def open_modificar_agente(self):
        # Crear una nueva ventana para modificar la información del agente
        modificar_agente_window = tk.Toplevel(self.root)
        app = ModificarAgenteApp(modificar_agente_window)

    def open_registrar_regimen(self):
        # Crear una nueva ventana para el registro de regímenes fiscales
        nuevo_regimen_window = tk.Toplevel(self.root)
        app = RegimenesFiscales(nuevo_regimen_window)

    def open_agent_list(self):
        agent_list_window = tk.Toplevel(self.root)
        app = AgentListApp(agent_list_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = PrincipalAdmin(root)
    root.mainloop()
