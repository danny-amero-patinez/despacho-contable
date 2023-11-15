import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

from NuevoCliente import AddClientApp
#from Cliente import Cliente
#from Emprendedor import Emprendedor

class Cambiar:
    def __init__(self, root):
        self.root = root
        self.root.title("Cambiar de cliente a emprendedor")

        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        ancho_ventana = 700
        alto_ventana = 400

        x = (ancho_pantalla - ancho_ventana) //2
        y = (alto_pantalla - alto_ventana) // 2

        self.root.geometry(f"{ancho_pantalla - ancho_ventana}x{alto_pantalla - alto_ventana}+{x}+{y}")

        colorMarco = "#009680"
        colorLabel = "#000000"
        colorBoton = "#607d88"
        colortextoboton = "#000000"

        self.root.configure(bg=colorMarco)

        marco = tk.Frame(root, padx=20, pady=20, bg=colorMarco)
        marco.pack(expand=True, fill="both")

      #  letraLabel = Font(family="arial", size=14)
      #  letraLabel2 = Font(family="arial", size=12)
      #  letraLabel3 = Font(family="arial", size=11)

        tituloLabel = tk.Label(marco, text="Informacion Cliente", bg=colorMarco, fg=colorLabel, font=("arial",11))
        tituloLabel.grid(row=0, column=1, sticky="w",pady=5, ipadx=70)

        idLabel = tk.Label(marco, text="ID Cliente", bg=colorMarco, fg=colorLabel, font=("arial",11))
        idLabel.grid(row=1, column=1, sticky="w",pady=5, ipadx=70)

        nombreLabel = tk.Label(marco, text="Nombre", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nombreLabel.grid(row=2, column=1, sticky="w",pady=5, ipadx=70)

        negocioLabel = tk.Label(marco, text="Nombre del negocio", bg=colorMarco, fg=colorLabel, font=("arial",11))
        negocioLabel.grid(row=3, column=1, sticky="w",pady=5, ipadx=70)

        correoLabel = tk.Label(marco, text="Correo", bg=colorMarco, fg=colorLabel, font=("arial",11))
        correoLabel.grid(row=4, column=1, sticky="w",pady=5, ipadx=70)

        rfcLabel = tk.Label(marco, text="RFC", bg=colorMarco, fg=colorLabel, font=("arial",11))
        rfcLabel.grid(row=5, column=1, sticky="w",pady=5, ipadx=70)

        nssLabel = tk.Label(marco, text="NSS", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nssLabel.grid(row=6, column=1, sticky="w",pady=5, ipadx=70)

        postalLabel = tk.Label(marco, text="Codigo Postal", bg=colorMarco, fg=colorLabel, font=("arial",11))
        postalLabel.grid(row=7, column=1, sticky="w",pady=5, ipadx=70)

        direccionLabel = tk.Label(marco, text="Direccion", bg=colorMarco, fg=colorLabel, font=("arial",11))
        direccionLabel.grid(row=8, column=1, sticky="w",pady=5, ipadx=70)


      #  idLabel = tk.Label(marco, text=f"ID Cliente: {id}", bg=colorMarco, fg=colorLabel, font=letraLabel)
      #  idLabel.grid()
       # idLabel.grid(row=2, column=0, sticky="w", pady=10, ipadx=5)

      #  nombreLabel = tk.Label(marco, text=f"Nombre: {nombre}", bg=colorMarco, fg=colorLabel, font=letraLabel)
      #  nombreLabel.grid()
      #  nombreLabel.grid(row=3, column=0, sticky="w", pady=10, ipadx=5)

      #  apellidoLabel = tk.Label(marco, text=f"apellido: {apellido}", bg=colorMarco, fg=colorLabel, font=letraLabel)
      #  apellidoLabel.grid()
       # apellidoLabel.grid(row=4, column=0, sticky="w", pady=10, ipadx=5)

      #  direccionLabel = tk.Label(marco, text=f"Direccion: {direccion}", bg=colorMarco, fg=colorLabel, font=letraLabel)
      #  direccionLabel.grid()
      #  direccionLabel.grid(row=5, column=0, sticky="w", pady=10, ipadx=5)

      #  regimenLabel = tk.Label(marco, text=f"Regimen fiscal: {regimen}", bg=colorMarco, fg=colorLabel, font=letraLabel)
      #  regimenLabel.grid()
      #  regimenLabel.grid(row=6, column=0, sticky="w", pady=10, ipadx=5)

      #  clienteLabel = tk.Label(marco, text="Informacion cliente ", bg=colorMarco, fg=colorLabel, font=letraLabel2)
      #  clienteLabel.grid(row=1, column=0, sticky="w", pady=20)

      #  def show_info(self, id, nombre, apellido, direccion, regimen):
      #    info = f"id cliente{id}\nNombre: {nombre}\nApellido: {apellido}\nDireccion: {direccion}\nRegimen Fiscal: {regimen}"

    #    datosLabel = tk:
     #   datos.Label = tk.Label(marco, text=f"ID cliente: {id}\nNombre: {nombre}\nApellido: {apellido}\nDirección: {direccion}\nRegimen Fiscal: {regimen}", bg=colorMarco, fg=colorLabel, font=letraLabel2)
    #    datosLabel.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

     #   idButton = tk.Button(marco, text="", bg=colorBoton, command=self.idboton)
     #   idButton.grid(row=4, column=1, sticky="w",pady=50, ipadx=40)
        
        #emprendedorLabel = pygame.font.SysFont("arial", 30)

if __name__ == "__main__":
    root = tk.Tk()
    app = Cambiar(root)
    root.mainloop()


