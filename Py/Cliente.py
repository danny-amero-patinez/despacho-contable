import tkinter as tk
from tkinter.font import Font 

class Cliente:
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
       # self.clienteLabel = Font(family="arial", size=50, weight="bold", slant="italic")
       # clienteLabel = tkFont.Font(family="Arial", size=16, weight="bold", slant="arial")
       # clienteLabel.configure(font=clienteLabel)
if __name__ == "__main__":
    root = tk.Tk()
    app = Cliente(root)
    root.mainloop()