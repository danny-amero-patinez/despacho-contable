import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

#-
from Cambiar_cliente_enprendedor import Cambiar

class Emprendedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Emprendedor")

        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        ancho_ventana = 900
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

        letraLabel = Font(family="arial", size=14)
        letraLabel2 = Font(family="arial", size=11)

        emprendedorLabel = tk.Label(marco, text="Emprendedor", bg=colorMarco, fg=colorLabel, font=letraLabel)
        emprendedorLabel.grid(row=4, column=1, sticky="w", ipadx=150)

        infoEmprendedorLabel = tk.Label(marco, text="Informacion de emprendedor", bg=colorMarco, fg=colorLabel, font=letraLabel2)
        infoEmprendedorLabel.grid(row=6, column=1, sticky="w", ipadx=10)

        nombrelabel = tk.Label(marco, text="Nombre:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nombrelabel.grid(row=8, column=1, sticky="w", ipadx=10)

        negociolabel = tk.Label(marco, text="Nombre del negocio:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        negociolabel.grid(row=9, column=1, sticky="w", ipadx=10)

        telefonolabel = tk.Label(marco, text="Telefono:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        telefonolabel.grid(row=10, column=1, sticky="w", ipadx=10)

        correolabel = tk.Label(marco, text="Correo:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        correolabel.grid(row=11, column=1, sticky="w", ipadx=10)

        rfclabel = tk.Label(marco, text="RFC:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        rfclabel.grid(row=12, column=1, sticky="w", ipadx=10)

        nsslabel = tk.Label(marco, text="NSS:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nsslabel.grid(row=13, column=1, sticky="w", ipadx=10)

        postallabel = tk.Label(marco, text="Codigo Postal:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        postallabel.grid(row=14, column=1, sticky="w", ipadx=10)

        capitallabel = tk.Label(marco, text="Capital inicial:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        capitallabel.grid(row=15, column=1, sticky="w", ipadx=10)

        tipoPersonalabel = tk.Label(marco, text="Tipo de persona:", bg=colorMarco, fg=colorLabel, font=("arial",11))
        tipoPersonalabel.grid(row=16, column=1, sticky="w", ipadx=10)

      #  emprendedorLabel = Font(family="Arial", size=15)
        #emprendedorLabel = pygame.font.SysFont("arial", 30)
if __name__ == "__main__":
    root = tk.Tk()
    app = Emprendedor(root)
    root.mainloop()