import tkinter as tk
from tkinter.font import Font 
from PIL import ImageTk, Image
class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente")

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

        self.clienteLabel = tk.Label(marco, text="Cliente", bg=colorMarco, fg=colorLabel, font=letraLabel)
        self.clienteLabel.grid(row=4, column=5, sticky="w", ipadx= 175)

        idlabel = tk.Label(marco, text="ID cliente: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        idlabel.grid(row=5, column=5, sticky="w", ipadx=10)

        nombrelabel = tk.Label(marco, text="Nombre: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nombrelabel.grid(row=6, column=5, sticky="w", ipadx=10)

        negociolabel = tk.Label(marco, text="Nombre del negocio: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        negociolabel.grid(row=7, column=5, sticky="w", ipadx=10)

        telefonolabel = tk.Label(marco, text="Telefono: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        telefonolabel.grid(row=8, column=5, sticky="w", ipadx=10)

        correolabel = tk.Label(marco, text="Correo: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        correolabel.grid(row=9, column=5, sticky="w", ipadx=10)

        rfclabel = tk.Label(marco, text="Nombre del negocio: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        rfclabel.grid(row=10, column=5, sticky="w", ipadx=10)

        nsslabel = tk.Label(marco, text="NSS: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nsslabel.grid(row=11, column=5, sticky="w", ipadx=10)

        postallabel = tk.Label(marco, text="Codigo Postal: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        postallabel.grid(row=12, column=5, sticky="w", ipadx=10)

        direccionlabel = tk.Label(marco, text="Direccion: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        direccionlabel.grid(row=13, column=5, sticky="w", ipadx=10)

        regimenlabel = tk.Label(marco, text="Regimen Fiscal: ", bg=colorMarco, fg=colorLabel, font=("arial",11))
        regimenlabel.grid(row=14, column=5, sticky="w", ipadx=10)

       # self.clienteLabel = Font(family="arial", size=50, weight="bold", slant="italic")
       # clienteLabel = tkFont.Font(family="Arial", size=16, weight="bold", slant="arial")
       # clienteLabel.configure(font=clienteLabel)
if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()