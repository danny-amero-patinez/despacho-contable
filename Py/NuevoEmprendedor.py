import random
import tkinter as tk
from tkinter import Label, messagebox
from tkinter import ttk
from PIL import ImageTk, Image

import mysql.connector

# Lista de regímenes fiscales en México
regimenes_fiscales = ["Régimen General de Ley", "Régimen de Incorporación Fiscal (RIF)",
                      "Régimen de Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras",
                      "Régimen de Arrendamiento", "Régimen de Sueldos y Salarios",
                      "Régimen de Personas Morales con Fines No Lucrativos",
                      "Régimen de Consolidación Fiscal", "Régimen de Actividades Empresariales y Profesionales",
                      "Régimen de Intereses", "Régimen de Dividendos"]

class AddEntrepreneur:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Emprendedor")

        # Obtiene el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana en la pantalla
        window_width = 400
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Colores personalizados de la paleta
        color_frame = "#009688"  # VERDE PRIMARIO
        color_label = "#FFFFFF"  # BLANCO
        color_button = "#607D8B"  # GRIS OSCURO
        color_button_text = "#000000"  # BLANCO

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

        name_label2 = tk.Label(frame, text="Nombre del Negocio:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label2.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.name_entry2 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry2.grid(row=2, column=1, padx=10, pady=5)

        name_label3 = tk.Label(frame, text="Teléfono:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label3.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        self.name_entry3 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry3.grid(row=3, column=1, padx=10, pady=5)

        name_label4 = tk.Label(frame, text="Correo 1:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label4.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.name_entry4 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry4.grid(row=4, column=1, padx=10, pady=5)

        name_label5 = tk.Label(frame, text="RFC:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label5.grid(row=5, column=0, sticky="w", padx=10, pady=5)

        self.name_entry5 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry5.grid(row=5, column=1, padx=10, pady=5)

        name_label6 = tk.Label(frame, text="NSS:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label6.grid(row=6, column=0, sticky="w", padx=10, pady=5)

        self.name_entry6 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry6.grid(row=6, column=1, padx=10, pady=5)

        name_label7 = tk.Label(frame, text="Código Postal:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label7.grid(row=7, column=0, sticky="w", padx=10, pady=5)

        self.name_entry7 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry7.grid(row=7, column=1, padx=10, pady=5)

        name_label13 = tk.Label(frame, text="Capital Inicial:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label13.grid(row=8, column=0, sticky="w", padx=10, pady=5)

        self.name_entry8 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry8.grid(row=8, column=1, padx=10, pady=5)

        regimen_label = tk.Label(frame, text="Tipo de Persona:", bg=color_frame, fg=color_label, font=("Arial", 12))
        regimen_label.grid(row=9, column=0, sticky="w", padx=10, pady=5)

        # Opciones para el combobox (seleccionar el tipo de persona)
        self.name_entry9 = ttk.Combobox(frame, values=["Persona Moral", "Persona Física"], font=("Arial", 12))
        self.name_entry9.grid(row=9, column=1, padx=10, pady=5)

        producto_checkbox = tk.Checkbutton(frame, text="Producto", font=("Arial", 12))
        producto_checkbox.grid(row=10, column=0, sticky="w", padx=10, pady=5)

        marketing_checkbox = tk.Checkbutton(frame, text="Marketing", font=("Arial", 12))
        marketing_checkbox.grid(row=10, column=1, sticky="w", padx=10, pady=5)

        equipo_checkbox = tk.Checkbutton(frame, text="Equipo de Trabajo", font=("Arial", 12))
        equipo_checkbox.grid(row=10, column=2, sticky="w", padx=10, pady=5)

        name_label12 = tk.Label(frame, text="Observaciones:", bg=color_frame, fg=color_label, font=("Arial", 12))
        name_label12.grid(row=11, column=0, sticky="w", padx=10, pady=5)

        self.name_entry10 = tk.Entry(frame, font=("Arial", 12))
        self.name_entry10.grid(row=11, column=1, padx=10, pady=5)

        register_button = tk.Button(frame, text="Registrar", command=self.register_Entrepreneur, bg=color_button,
                                    fg=color_button_text, font=("Arial", 12))
        register_button.grid(row=15, column=0, columnspan=2, pady=10)

        frame.update_idletasks()
        window_width = frame.winfo_reqwidth() + 40
        window_height = frame.winfo_reqheight() + 40
        self.root.geometry(f"{window_width}x{window_height}")

    def generate_id(self):
        return str(random.randint(10000000, 9999999999))

    def insert_variables_into_table(
            self, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10
    ):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='lion',
                                                 user='root',
                                                 password='panconl3ch3.')
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO emprendedores (
            NombreProyecto, Giro, Direccion, Regimen, InovacionTecnologica, 
            Pm, Pf, Gestion, Producto, 
            Marketing, EquipoTrabajo, Observaciones, CapitalInicial
            )
                                    VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            ) """

            record = (v1, v2, v3, v4, v5, "", "", "", "", "", "", v6, "")
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into emprendedores table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                # print("MySQL connection is closed")

    def register_Entrepreneur(self, producto_checkbox=None, marketing_checkbox=None, equipo_checkbox=None):
        self.insert_variables_into_table(
            self.name_entry.get(), self.name_entry2.get(), self.name_entry3.get(),
            self.name_entry4.get(), self.name_entry5.get(), self.name_entry6.get(),
            self.name_entry7.get(), self.name_entry8.get(), self.name_entry9.get(),
            self.name_entry10.get()
            # self.direccion_entry.get(), self.regimen_combobox.get(),
            # "Producto" if producto_checkbox.get() else "",
            # "Marketing" if marketing_checkbox.get() else "",
            # "Equipo de Trabajo" if equipo_checkbox.get() else "",
            # self.name_entry12.get(), self.name_entry13.get()
        )

        id = self.generate_id()

        messagebox.showinfo("Registro Exitoso!")

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AddEntrepreneur(root)
    root.mainloop()
