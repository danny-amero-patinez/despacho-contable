import tkinter as tk
from tkinter import ttk, Text, END, messagebox, StringVar
import mysql.connector
from PIL import ImageTk, Image


class AgentListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Agentes")

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

        # Etiqueta de título
        title_label = tk.Label(frame, text="Lista de Agentes", font=("Helvetica", 20), bg=color_frame, fg=color_label)
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 30))

        # Widget de texto para mostrar la lista de agentes
        self.agent_list_text = Text(frame, bg=color_frame, fg=color_button_text)
        self.agent_list_text.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Botón para cargar la lista de agentes
        load_button = ttk.Button(frame, text="Cargar Agentes", command=self.load_agents, style="Custom.TButton")
        load_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

        # Botón para mostrar/ocultar contraseñas
        self.show_passwords = StringVar()
        show_passwords_button = ttk.Checkbutton(frame, text="Mostrar Contraseñas", variable=self.show_passwords,
                                                command=self.toggle_password_visibility)
        show_passwords_button.grid(row=3, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

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

    def load_agents(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='lion',
                                                 user='root',
                                                 password='panconl3ch3')

            sql_select_Query = "select * from clientes"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            self.agent_list_text.delete(1.0, END)
            query = ""

            for row in records:
                row = str("ID del Agente = " + str(row[0]) +
                          "\n" + "Nombre Completo = " + row[1] +
                          "\n" + "Usuario = " + row[2] +
                          "\n" + "Contraseña = " + "*" * len(row[3]) if not self.show_passwords.get() else row[3] +
                          "\n" + "RFC = " + row[4] +
                          "\n" + "NSS = " + row[5] +
                          "\n" + "observaciones = " + row[6] +
                          "\n\n\n")

                query += row

            self.agent_list_text.insert(END, query)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Error reading data from MySQL table.")
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    def toggle_password_visibility(self):
        self.load_agents()  # Recargar la lista de agentes para aplicar la visibilidad de contraseñas


if __name__ == "__main__":
    root = tk.Tk()
    app = AgentListApp(root)
    root.mainloop()
