import tkinter as tk
from tkinter.font import Font

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
      #  emprendedorLabel = Font(family="Arial", size=15)
        #emprendedorLabel = pygame.font.SysFont("arial", 30)
if __name__ == "__main__":
    root = tk.Tk()
    app = Emprendedor(root)
    root.mainloop()