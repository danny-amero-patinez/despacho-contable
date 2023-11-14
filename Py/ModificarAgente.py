import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk, Image

class ModificarAgenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modificar Agente")

        # Conexión a la base de datos
        self.connection = mysql.connector.connect(host='localhost', database='lion', user='root',
                                                  password='panconl3ch3.')

        # Datos simulados para los agentes (deberías cargar los datos reales desde la base de datos)
        self.agentes = self.get_agentes_from_database()

        self.selected_agente_id = tk.StringVar()
        self.show_password = tk.BooleanVar()

        frame = ttk.Frame(root, style="Custom.TFrame")
        frame.pack(expand=True, fill="both")

        # Widgets para seleccionar el agente
        ttk.Label(frame, text="Seleccione un Agente:", style="Custom.TLabel").pack(pady=(20, 5))
        agente_combobox = ttk.Combobox(frame, textvariable=self.selected_agente_id,
                                       values=[agente["id"] for agente in self.agentes], style="Custom.TCombobox")
        agente_combobox.bind("<<ComboboxSelected>>", lambda event: self.cargar_datos_agente_seleccionado())
        agente_combobox.pack(pady=5)

        # Widgets para modificar la información del agente
        ttk.Label(frame, text="Nombre Completo:", style="Custom.TLabel").pack(pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.nombre_var, style="Custom.TEntry").pack(pady=5)

        ttk.Label(frame, text="Nombre de usuario:", style="Custom.TLabel").pack(pady=5)
        self.usuario_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.usuario_var, style="Custom.TEntry").pack(pady=5)

        ttk.Label(frame, text="Contraseña:", style="Custom.TLabel").pack(pady=5)
        self.contraseña_var = tk.StringVar()
        entry = ttk.Entry(frame, textvariable=self.contraseña_var, show="*" if not self.show_password.get() else "",
                          style="Custom.TEntry")
        entry.pack(pady=5)

        show_password_checkbox = ttk.Checkbutton(frame, text="Mostrar Contraseña", variable=self.show_password,
                                                 style="Custom.TCheckbutton", command=self.toggle_password_visibility)
        show_password_checkbox.pack(pady=5)

        ttk.Label(frame, text="RFC:", style="Custom.TLabel").pack(pady=5)
        self.rfc_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.rfc_var, style="Custom.TEntry").pack(pady=5)

        ttk.Label(frame, text="NSS:", style="Custom.TLabel").pack(pady=5)
        self.nss_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.nss_var, style="Custom.TEntry").pack(pady=5)

        ttk.Label(frame, text="Observaciones:", style="Custom.TLabel").pack(pady=5)
        self.observaciones_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.observaciones_var, style="Custom.TEntry").pack(pady=5)

        save_button = ttk.Button(frame, text="Guardar Cambios", command=self.guardar_cambios, style="Custom.TButton")
        save_button.pack(pady=(20, 10))

        # Centrar la ventana en la pantalla
        window_width = 400
        window_height = 550
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def get_agentes_from_database(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql_select_Query = "SELECT * FROM clientes"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            return records
        except mysql.connector.Error as e:
            print("Error fetching data from MySQL table: {}".format(e))
        finally:
            if cursor:
                cursor.close()

    def cargar_datos_agente_seleccionado(self, event):
        # Obtén el ID del agente seleccionado
        selected_id = int(self.selected_agente_id.get() if self.select_agente_id.get() else -1)

        # Busca el agente seleccionado en los datos simulados
        for agente in self.agentes:
            if agente["id"] == selected_id:
                # Llena los campos con la información del agente seleccionado
                self.nombre_var.set(agente["NombresCompletos"])  # Corregido aquí
                self.usuario_var.set(agente["usuario"])
                self.contraseña_var.set(agente["contraseña"])
                self.rfc_var.set(agente["rfc"])
                self.nss_var.set(agente["nss"])
                self.observaciones_var.set(agente["observaciones"])

    def guardar_cambios(self):
        try:
            # Agrega la lógica para guardar los cambios en la base de datos
            cursor = self.connection.cursor()

            # Ejemplo: Actualizar el nombre y la contraseña del agente seleccionado
            update_query = "UPDATE clientes SET NombresCompletos = %s, Contraseña = %s WHERE id = %s"
            cursor.execute(update_query,
                           (self.nombre_var.get(), self.contraseña_var.get(), self.selected_agente_id.get()))

            self.connection.commit()
            mensaje = "Se han guardado los cambios para el agente {}".format(self.selected_agente_id.get())
            messagebox.showinfo("Cambios Guardados", mensaje)
        except mysql.connector.Error as e:
            print("Error updating data in MySQL table: {}".format(e))
        finally:
            if cursor:
                cursor.close()

    def toggle_password_visibility(self):
        # Actualiza la visibilidad de la contraseña al hacer clic en el checkbox
        self.cargar_datos_agente_seleccionado(None)
        entry = self.root.focus_get()
        entry.config(show="*" if not self.show_password.get() else "")

    def __del__(self):
        # Cierre de la conexión cuando se destruye la instancia
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    root = tk.Tk()

    # Estilo personalizado
    s = ttk.Style()
    s.configure("Custom.TFrame", background="#009688")
    s.configure("Custom.TLabel", background="#009688", foreground="#FFFFFF")
    s.configure("Custom.TEntry", fieldbackground="#FFFFFF")
    s.configure("Custom.TButton", background="#607D8B", foreground="#FFFFFF")
    s.configure("Custom.TCombobox", fieldbackground="#FFFFFF")
    s.configure("Custom.TCheckbutton", background="#009688", foreground="#FFFFFF")

    app = ModificarAgenteApp(root)
    root.mainloop()
