import tkinter as tk
from tkinter import ttk, Text, END, messagebox, Label
from PIL import ImageTk, Image
import mysql.connector


class ClientListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Clientes")

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
        # Importacion de la imagen y redimensionamiento
        imagenImportada = Image.open("Logo 1.png")
        imagenRedimensionada = imagenImportada.resize((128,128), Image.BILINEAR)
        imagen_Logo = ImageTk.PhotoImage(imagenRedimensionada)
        # Etiqueta contenedora de Logo
        etiqueta_logo = Label(frame, image= imagen_Logo, bg='WHITE')
        etiqueta_logo.noMeBorresCrack= imagen_Logo
        etiqueta_logo.grid(row=0, column=0, padx=10, pady=10)

        # Etiqueta de título
        title_label = tk.Label(frame, text="Lista de Clientes", font=("Helvetica", 20), bg=color_frame, fg=color_label)
        title_label.grid(row=1, column=0, columnspan=2, pady=(20, 30))

        # Widget de texto para mostrar la lista de clientes
        self.client_list_text = Text(frame, bg=color_frame, fg=color_button_text)
        self.client_list_text.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Botón para cargar la lista de clientes
        load_button = ttk.Button(frame, text="Cargar Clientes", command=self.load_clients, style="Custom.TButton")
        load_button.grid(row=3, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

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

    def load_clients(self):
        # Leer los clientes desde el archivo clientes.txt

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='lion',
                                                 user='root',
                                                 password='panconl3ch3.')

            sql_select_Query = "select * from clientes"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            # print("Total number of rows in table: ", cursor.rowcount)

            # print("\nPrinting each row")
            self.client_list_text.delete(1.0, END)
            query = ""

            for row in records:
                row = str("Id del cliente = " + str(row[0]) +
                        "\n" + "Fecha = " + str(row[1]) +
                        "\n" + "Nombres completos = " + row[2] +
                        "\n" + "Nombre del negocio = " + row[3] +
                        "\n" + "Celular 1 = " + row[4] +
                        "\n" + "Celular 2 = " + row[5] +
                        "\n" + "Telefono 1 = " + row[6] +
                        "\n" + "Correo 1 = " + row[7] +
                        "\n" + "Correo 2 = " + row[8] +
                        "\n" + "Ciudad = " + row[9] +
                        "\n" + "Dirección = " + row[10] +
                        "\n" + "RFC = " + row[11] +
                        "\n" + "Regimen = " + row[12] +
                        "\n" + "NSS = " + row[13] +
                        "\n" + "CP = " + row[14] + "\n\n\n")

                query += row

            self.client_list_text.insert(END, query)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Error reading data from MySQL table.")
            # print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                # print("MySQL connection is closed")

        # try:
            # with open("clientes.txt", "r") as file:
                # client_data = file.read()
                # self.client_list_text.delete(1.0, END)  # Limpiar el widget de texto
                # self.client_list_text.insert(END, client_data)
        # except FileNotFoundError:
            # messagebox.showerror("Error", "El archivo clientes.txt no existe.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ClientListApp(root)
    root.mainloop()
