import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector
#from tkinter import tkk

from principalAdmin import principalAdmin

class RegimenesFiscales:
  def __init__(self, root):
    self.root = root
    self.root.title("Definir regimenes fiscales")

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
    color_texto_boton = "#000000"

    self.root.configure(bg=colorMarco)

    frame = tk.Frame(root, padx=20, pady=20, bg=colorMarco)
    frame.pack(expand=True, fill="both")

    idRegimenLabel = tk.Label(frame, text=" ID Regimen: ", bg=colorMarco, fg=colorLabel)
    idRegimenLabel.grid(row=1, column=0, sticky="ww")

  #  self.id = tk.Entry(frame)
  #  self.id.grid(row=1, column=1, sticky="ww", ipadx=1, pady=30)

    self.Idlabel = tk.Label(frame, bg=colorMarco, fg=colorLabel)
    self.Idlabel.grid(row=1, column=1, sticky="ww")

    regimenLabel = tk.Label(frame, text="Escribir regimen: ", bg=colorMarco, fg=colorLabel)
    regimenLabel.grid(row=2, column=0, sticky="w")

    self.regimen = tk.Entry(frame)
    self.regimen.grid(row=2, column=1, sticky="w", ipadx=50, pady=20)

    idBoton = tk.Button(frame, text="Generar ID", command=self.botonid, bg=colorBoton, fg=color_texto_boton)
    idBoton.grid(row=1, column=2, columnspan=40, pady=10, ipadx=20)

    registrarBoton = tk.Button(frame, text="Registrar regimen", command=self.registroRegimen, bg=colorBoton, fg=color_texto_boton)
    registrarBoton.grid(row=3, column=1, columnspan=1, pady=30, ipadx=20) 
   # self.registrarBoton.place(x=60, y=40)

    eliminarBoton = tk.Button(frame, text="Eliminar regimen", command=self.eliminarRegimen, bg=colorBoton, fg=color_texto_boton)
    eliminarBoton.grid(row=20, column=1, columnspan=4, pady=20, ipadx=20)

  def botonid(self):
    resultadoId = (random.randint(1,100000000000))
    self.Idlabel.configure(text=resultadoId)
  # print(random.randint(0,100))
  #  Id = self.Id.set() 

  def registroRegimen(self):
      conexion = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password = '<password>',
        database = '<database>'
      )

      cursor = conexion.cursor()

      consulta = "INSERT INTO regimen (idRegimen, Regimen) values (%s, %s)"

      dato = "id"
      dato2 = "regimen"

      cursor.execute(consulta (dato, dato2))

      conexion.commit()

      cursor.close()
      conexion.close()
      
      regimen = self.regimen.get()
      #print("registro exitoso: {regimen}")

      messagebox.showinfo(message="El rigimen fue agregado exitosamente", title="Regimen")
    #  self.root.destroy()

  def eliminarRegimen(self):
      regimen = self.regimen.get()
     #print("Elimino el regimen: {regimen}")
      messagebox.showerror(message="El regimen se elimino correctamente", title="Regimen")

      self.root.destroy()

if __name__ == "__main__":
  root = tk.Tk()
  app = RegimenesFiscales(root)
  root.mainloop()
