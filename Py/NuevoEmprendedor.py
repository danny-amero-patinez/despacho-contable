import tkinter as tk
from tkinter import messagebox
import mysql.connector


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
        name_label = tk.Label(frame, text="Nombre del proyecto:", bg=color_frame, fg=color_label)
        name_label.grid(row=1, column=0, sticky="w")

        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        last_name_label = tk.Label(frame, text="Regimen:", bg=color_frame, fg=color_label)
        last_name_label.grid(row=2, column=0, sticky="w")

        self.last_name_entry = tk.Entry(frame)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")



        name_label2 = tk.Label(frame, text="Direccion:", bg=color_frame, fg=color_label)
        name_label2.grid(row=3, column=0, sticky="w")

        self.name_entry2 = tk.Entry(frame)
        self.name_entry2.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        last_name_label2 = tk.Label(frame, text="Giro:", bg=color_frame, fg=color_label)
        last_name_label2.grid(row=4, column=0, sticky="w")

        self.last_name_entry2 = tk.Entry(frame)
        self.last_name_entry2.grid(row=4, column=1, padx=10, pady=5, sticky="w")


        # Botón para registrar el emprendedor
        register_button = tk.Button(frame, text="Registrar", command=self.register_entrepreneur, bg=color_button,
                                    fg=color_button_text)
        register_button.grid(row=6, column=0, columnspan=2, pady=10)

    def insert_variables_into_table(
            self, v1, v2, v3, v4
    ):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='?',
                                                 user='root',
                                                 password='?')
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO emprendedores (
            NombreProyecto, Regimen, Direccion, Giro
            ) 
                                    VALUES (
            %s, %s, %s, %s
            ) """


            record = (v1, v2, v3, v4)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into Laptop table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def register_entrepreneur(self):
        # Obtener los valores ingresados por el usuario
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()

        self.insert_variables_into_table(
            self.name_entry.get(), self.last_name_entry.get(),
            self.name_entry2.get(), self.last_name_entry2.get()
        );

        # Guardar la información del emprendedor en un archivo de texto
        # with open("emprendedores.txt", "a") as file:
            # file.write(f"Nombre: {name}\nApellido: {last_name}\n\n")

        # Mostrar un mensaje de confirmación
        # message = f"Emprendedor registrado:\nNombre: {name}\nApellido: {last_name}"
        messagebox.showinfo("Registro Exitoso!")

        # Cerrar la ventana de registro de emprendedores
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AddEntrepreneurApp(root)
    root.mainloop() 
