import tkinter as tk
import tkinter as tkk
import tkinter as messagebox

class AtencionesEmprendedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar atenciones al emprendedor")

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

        atencionesLabel = tk.Label(marco, text="Atenciones a emprendedores", bg=colormarco, fg=colorletra, font=("arial", 14))
        atencionesLabel.grid(row=1, columns=1, sticky="w", padx=100, pady=10)

        nombrelabel = tk.Label(marco, text="Nombre: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        nombrelabel.grid(row=2, columns=1, sticky="w", padx=20, pady=10)

        self.nombre = tk.Entry(marco)
        self.nombre.grid(row=2, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        rfclabel = tk.Label(marco, text="RFC: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        rfclabel.grid(row=3, columns=1, sticky="w", padx=20, pady=10)

        self.rfc = tk.Entry(marco)
        self.rfc.grid(row=3, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        fechalabel = tk.Label(marco, text="Fecha: ", bg=colormarco, fg=colorletra, font=("arial",11))
        fechalabel.grid(row=4, columns=1, sticky="w", padx=20, pady=10)

        self.fecha = tk.Entry(marco)
        self.fecha.grid(row=4, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        celLabel = tk.Label(marco, text="Numero de telefono: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        celLabel.grid(row=5, columns=1, sticky="w", padx=20, pady=10)

        self.cel = tk.Entry(marco)
        self.cel.grid(row=5, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        correolabel = tk.Label(marco, text="Correo electronico: ", bg=colormarco, fg=colorletra, font=("arial",11))
        correolabel.grid(row=6, columns=1, sticky="w", padx=20, pady=10)

        self.correo = tk.Entry(marco)
        self.correo.grid(row=6, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        descripcionlabel = tk.Label(marco, text="Observaciones: ", bg=colormarco, fg=colorletra, font=("arial",11))
        descripcionlabel.grid(row=7, columns=1, sticky="w", padx=20, pady=10)

        self.descripcion = tk.Entry(marco)
        self.descripcion.grid(row=7, columns=1, sticky="w", ipadx=50, padx=200, pady=10)

        registrarAtencionBoton = tk.Button(marco, text="Registrar Atencion al emprendedor", command=self.registrarAtencion, bg=colorboton, fg=colorletraboton)
        registrarAtencionBoton.grid(row=10, columnspan=1, sticky="w", padx=150, pady=5)


    def registrarAtencion(self):
        messagebox.showinfo("registro de atencion al emprendedor, registrado", messagebox)



if __name__ == "__main__":
    root = tk.Tk()
    app = AtencionesEmprendedor(root)
    root.mainloop()

    