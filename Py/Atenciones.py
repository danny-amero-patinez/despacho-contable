import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Label, messagebox

class Atenciones:
    def __init__(self, root):
        self.root = root
        self.root.title("Atenciones al cliente")

        anchoPantalla = root.winfo_screenwidth()
        altoPantalla = root.winfo_reqheight()

        anchoVentana = 500
        altoventana = 400

        x = (anchoPantalla - anchoVentana) // 2
        y = (altoPantalla - altoventana) // 2

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
        # Etiqueta contenedora de Logo
        etiqueta_logo = Label(marco, image=imagen_Logo, bg='WHITE')
        etiqueta_logo.noMeBorresCrack = imagen_Logo
        etiqueta_logo.grid(row=0, column=0, padx=10, pady=10)

        atencionesLabel = tk.Label(marco, text="Atenciones a clientes y emprendedores", bg=colormarco, fg=colorletra,
                                   font=("arial", 12))
        atencionesLabel.grid(row=1, columns=1, sticky="w", padx=100, pady=10)

        clientelabel = tk.Label(marco, text="Clientes", bg=colormarco, fg=colorletra, font=("arial", 12))
        clientelabel.grid(row=3, column=0, sticky="w", padx=80, pady=5)

        emprendedorlabel = tk.Label(marco, text="Emprendedores", bg=colormarco, fg=colorletra, font=("arial", 12))
        emprendedorlabel.grid(row=3, column=0, sticky="w", padx=280, pady=5)

        emprendedorBoton = tk.Button(marco, text="Atencion al Cliente", command=self.atencionCliente, bg=colorboton,
                                     fg=colorletraboton)
        emprendedorBoton.grid(row=8, columnspan=1, sticky="w", padx=50, pady=5)

        clienteBoton = tk.Button(marco, text="Atencion al Emprededor", command=self.atencionEmprendedor, bg=colorboton,
                                 fg=colorletra)
        clienteBoton.grid(row=8, columnspan=1, sticky="w", padx=285, pady=5)

    #  idlabel = tk.Label(marco, text="ID", bg=colormarco, fg=colorletra, font=("arial", 12))
    #  idlabel.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    def atencionCliente(self):
        atencionesC_window = tk.Toplevel(self.root)
        from AtencionesCliente import AtencionesCliente
        app = AtencionesCliente(atencionesC_window)
        ########################

    def atencionEmprendedor(self):
        atencionesE_window = tk.Toplevel(self.root)
        from AtencionesEmprendedor import AtencionesEmprendedor
        app = AtencionesEmprendedor(atencionesE_window)
        ###################################


if __name__ == "__main__":
    root = tk.Tk()
    app = Atenciones(root)
    root.mainloop()
