import tkinter as tk
# import tkinter as messagebox
from tkinter import Label, messagebox
import mysql.connector
from PIL import ImageTk, Image

class AtencionesCliente:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar atenciones al cliente")

        anchoPantalla = root.winfo_screenwidth()
        altoPantalla = root.winfo_screenheight()

        anchoVentana = 600
        altoventana = 550

        x = (anchoPantalla - anchoVentana) //2
        y = (altoPantalla - altoventana) //2

        self.root.geometry(f"{anchoVentana}x{altoventana}+{x}+{y}")

        colormarco = "#009688"
        colortitulo = "#000000"
        colorletra = "#000000"
        colorboton = "#608d7b"
        colorletraboton = "#000000"

        marco = tk.Frame(root, padx=40, pady=30, bg=colormarco)
        marco.pack(expand=True, fill="both")

        imagenImportada = Image.open("LogoB.png")
        imagenRedimensionada = imagenImportada.resize((128, 64), Image.BILINEAR)
        imagen_Logo = ImageTk.PhotoImage(imagenRedimensionada)
     #   Etiqueta contenedora de Logo
        etiqueta_logo = Label(marco, image=imagen_Logo, bg='WHITE')
        etiqueta_logo.noMeBorresCrack = imagen_Logo
        etiqueta_logo.grid(row=0, column=0, padx=10, pady=10)

        atencionesLabel = tk.Label(marco, text="Atenciones al cliente", bg=colormarco, fg=colorletra, font=("arial", 11))
        atencionesLabel.grid(row=1, columns=1, sticky="w", padx=120, pady=10)

        idlabel = tk.Label(marco, text="ID Cliente: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        idlabel.grid(row=2, columns=1, sticky="w", padx=20, pady=10)

        self.id = tk.Entry(marco)
        self.id.grid(row=2, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        nombrelabel = tk.Label(marco, text="Nombre: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        nombrelabel.grid(row=3, columns=1, sticky="w", padx=20, pady=10)

        self.nombre = tk.Entry(marco)
        self.nombre.grid(row=3, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        rfclabel = tk.Label(marco, text="RFC: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        rfclabel.grid(row=4, columns=1, sticky="w", padx=20, pady=10)

        self.rfc = tk.Entry(marco)
        self.rfc.grid(row=4, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        fechalabel = tk.Label(marco, text="Fecha: ", bg=colormarco, fg=colorletra, font=("arial",11))
        fechalabel.grid(row=5, columns=1, sticky="w", padx=20, pady=10)

        self.fecha = tk.Entry(marco)
        self.fecha.grid(row=5, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        celLabel = tk.Label(marco, text="Numero de telefono: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        celLabel.grid(row=6, columns=1, sticky="w", padx=20, pady=10)

        self.cel = tk.Entry(marco)
        self.cel.grid(row=6, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        correoLabel = tk.Label(marco, text="Corrreo electronico: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        correoLabel.grid(row=7, columns=1, sticky="w", padx=20, pady=10)

        self.correo = tk.Entry(marco)
        self.correo.grid(row=7, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        descripcionlabel = tk.Label(marco, text="Observaciones: ", bg=colormarco, fg=colorletra, font=("arial",11))
        descripcionlabel.grid(row=8, columns=1, sticky="w", padx=20, pady=10)

        self.descripcion = tk.Entry(marco)
        self.descripcion.grid(row=8, columns=1, sticky="w", ipadx=50, padx=200, pady=10)


        registrarAtencionBoton = tk.Button(marco, text="Registrar Atencion al cliente", command=self.registrarAtencion, bg=colorboton, fg=colorletraboton)
        registrarAtencionBoton.grid(row=10, columnspan=1, sticky="w", padx=130, pady=5)

    def registrarAtencion(self, v1, v2, v3, v4, v5, v6):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                database='lion',
                password='julianms3'
            )

            cursor = conexion.cursor()

            mysql_insert_query = "INSERT INTO atenciones (idCliente, Fecha, DetallesRelevantes) VALUES (%s, %s, %s)" 
            record = (v1, v2, "", "", "", "", "", v3, v4, v5, "", v6, "")
            print(record)
            cusor.exexute(mysql_insert_query, record)
            #id_Atencion = self.id.get("text")
            #Fecha = self.fecha.get()
            #cursor.execute(mysql_insert_query, (id_Atencion, Fecha))

            conexion.commit()
            print("Record inserted successfully into agentes table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
        finally:
            if conexion.is_connected:
                cursor.close()
                conexion.close()

        messagebox.showinfo("Registro", "Registro de atencion al cliente, registrado")


if __name__ == "__main__":
    root = tk.Tk()
    app = AtencionesCliente(root)
    root.mainloop()

    