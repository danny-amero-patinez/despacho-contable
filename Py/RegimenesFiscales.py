import tkinter as tk
from tkinter import messagebox, Label
import random
import mysql.connector
from PIL import ImageTk, Image

class RegimenesFiscales:
    def __init__(self, root):
        self.root = root
        self.root.title("Definir Regímenes Fiscales")

        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        ancho_ventana = 500
        alto_ventana = 400
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        colorMarco = "#009688"
        colorLabel = "#000000"
        colorBoton = "#607d8b"
        colorTextoBoton = "#000000"

        self.root.configure(bg=colorMarco)

        frame = tk.Frame(root, padx=20, pady=20, bg=colorMarco)
        frame.pack(expand=True, fill="both")
        
        # Importacion de la imagen y redimensionamiento
        imagenImportada = Image.open("LogoB.png")
        imagenRedimensionada = imagenImportada.resize((128,64), Image.BILINEAR)
        imagen_Logo = ImageTk.PhotoImage(imagenRedimensionada)
        # Etiqueta contenedora de Logo
        etiqueta_logo = Label(frame, image= imagen_Logo, bg='WHITE')
        etiqueta_logo.noMeBorresCrack= imagen_Logo
        etiqueta_logo.grid(row=0, column=0, padx=10, pady=10)

        idRegimenLabel = tk.Label(frame, text="ID del Régimen:", bg=colorMarco, fg=colorLabel)
        idRegimenLabel.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(30, 10))

        self.Idlabel = tk.Label(frame, bg=colorMarco, fg=colorLabel)
        self.Idlabel.grid(row=1, column=1, sticky="w", pady=(30, 10))

        regimenLabel = tk.Label(frame, text="Escribir Régimen:", bg=colorMarco, fg=colorLabel)
        regimenLabel.grid(row=2, column=0, sticky="w", padx=(0, 10), pady=(10, 10))

        self.regimen = tk.Entry(frame)
        self.regimen.grid(row=2, column=1, sticky="w", ipadx=50, pady=(10, 10))

        idBoton = tk.Button(frame, text="Generar ID", command=self.botonid, bg=colorBoton, fg=colorTextoBoton)
        idBoton.grid(row=1, column=2, pady=(30, 10), padx=(10, 0))

        registrarBoton = tk.Button(frame, text="Registrar Régimen", command=self.registroRegimen, bg=colorBoton,
                                   fg=colorTextoBoton)
        registrarBoton.grid(row=3, column=1, pady=(50, 30))

        eliminarBoton = tk.Button(frame, text="Eliminar Régimen", command=self.eliminarRegimen, bg=colorBoton,
                                  fg=colorTextoBoton)
        eliminarBoton.grid(row=4, column=1, pady=(10, 20))

    def botonid(self):
        resultadoId = random.randint(1, 99)
        self.Idlabel.configure(text=resultadoId)

    def registroRegimen(self):
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='<panconl3ch3.>',
            database='<lion>'
        )

        cursor = conexion.cursor()

        consulta = "INSERT INTO regimen (idRegimen, Regimen) VALUES (%s, %s)"
        id_regimen = self.Idlabel.cget("text")
        regimen = self.regimen.get()

        cursor.execute(consulta, (id_regimen, regimen))

        conexion.commit()

        cursor.close()
        conexion.close()

        messagebox.showinfo(message="El Régimen fue agregado exitosamente", title="Régimen")

    def eliminarRegimen(self):
        regimen = self.regimen.get()
        messagebox.showerror(message="El Régimen se eliminó correctamente", title="Régimen")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegimenesFiscales(root)
    root.mainloop()

