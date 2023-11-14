import tkinter as tk
from tkinter import Label, messagebox
import mysql.connector
import random
from PIL import ImageTk, Image

class AgenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Agente")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = 400
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        color_frame = "#009688"
        color_label = "#FFFFFF"
        color_button = "#607D8B"
        color_button_text = "#000000"

        frame = tk.Frame(root, padx=20, pady=20, bg=color_frame)
        frame.pack(expand=True, fill="both")

        imagenImportada = Image.open("LogoB.png")
        imagenRedimensionada = imagenImportada.resize((128, 64), Image.BILINEAR)
        imagen_Logo = ImageTk.PhotoImage(imagenRedimensionada)
        # Etiqueta contenedora de Logo
        etiqueta_logo = Label(frame, image=imagen_Logo, bg='WHITE')
        etiqueta_logo.noMeBorresCrack = imagen_Logo
        etiqueta_logo.grid(row=0, column=0, padx=10, pady=10)

        name_label = tk.Label(frame, text="Nombre Completo:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.name_entry = tk.Entry(frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        name_label2 = tk.Label(frame, text="Nombre de usuario:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label2.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.name_entry2 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry2.grid(row=2, column=1, padx=10, pady=5)

        name_label3 = tk.Label(frame, text="Contraseña:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label3.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        self.name_entry3 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry3.grid(row=3, column=1, padx=10, pady=5)

        name_label4 = tk.Label(frame, text="RFC:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label4.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.name_entry4 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry4.grid(row=4, column=1, padx=10, pady=5)

        name_label5 = tk.Label(frame, text="NSS:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label5.grid(row=5, column=0, sticky="w", padx=10, pady=5)

        self.name_entry5 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry5.grid(row=5, column=1, padx=10, pady=5)

        name_label6 = tk.Label(frame, text="Observaciones:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label6.grid(row=6, column=0, sticky="w", padx=10, pady=5)

        self.name_entry6 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry6.grid(row=6, column=1, padx=10, pady=5)

        register_button = tk.Button(frame, text="Registrar", command=self.registrar_agente, bg=color_button,
                                    fg=color_button_text, font=("Arial", 12))
        register_button.grid(row=7, column=0, columnspan=2, pady=10)

        frame.update_idletasks()
        window_width = frame.winfo_reqwidth() + 40
        window_height = frame.winfo_reqheight() + 40
        self.root.geometry(f"{window_width}x{window_height}")

    def generate_id(self):
        return str(random.randint(10000000, 9999999999))

    def insert_variables_into_table(self, v1, v2, v3, v4, v5, v6):
        try:
            connection = mysql.connector.connect(host='localhost', database='lion', user='root', password='panconl3ch3.')
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO agentes (
                    NombresCompletos, Password, NivelDeEstudios, NombreEscuela, 
                    EstadoDeSalud, Enfermedades, ConsumoSustancias, AntiguosEmpleos, 
                    Edad, Celular1, Celular2, Correo1, Correo2,
                    Direccion, Observaciones, Activo, NombreContacto, Hobbies
                    )
                                            VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    ) """

            record = (v1, v3, "", "", "", "", "", "", "", 0, "", v5, v4, "", v6, 0, v2, "")
            print(record)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into agentes table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                # print("MySQL connection is closed")

    def registrar_agente(self):
        self.insert_variables_into_table(
            self.name_entry.get(), self.name_entry2.get(), self.name_entry3.get(),
            self.name_entry4.get(), self.name_entry5.get(), self.name_entry6.get()
        )

        id = self.generate_id()
        messagebox.showinfo("Registro Exitoso!")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AgenteApp(root)
    root.mainloop()
