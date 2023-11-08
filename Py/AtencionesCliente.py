import tkinter as tk
import tkinter as messagebox

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

    def registrarAtencion(self):
        messagebox.showinfo("Registro de atencion al cliente, registrado", message)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = AtencionesCliente(root)
    root.mainloop()

    