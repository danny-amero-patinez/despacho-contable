import tkinter as tk
import tkinter as tkk
import tkinter as messagebox

class AtencionesEmprendedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar atenciones al emprendedor")

        anchoPantalla = root.winfo_screenwidth()
        altoPantalla = root.winfo_screenheight()

        anchoVentana = 500
        altoventana = 400

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

        idlabel = tk.Label(marco, text="ID Cliente: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        idlabel.grid(row=2, columns=1, sticky="w", padx=20, pady=10)

        nombrelabel = tk.Label(marco, text="Nombre: ", bg=colormarco, fg=colorletra, font=("arial", 11))
        nombrelabel.grid(row=3, columns=1, sticky="w", padx=20, pady=10)

        dialabel = tk.Label(marco, text="Dia: ", bg=colormarco, fg=colorletra, font=("arial",11))
        dialabel.grid(row=4, columns=1, sticky="w", padx=20, pady=10)

        meslabel = tk.Label(marco, text="Mes: ", bg=colormarco, fg=colorletra, font=("arial",11))
        meslabel.grid(row=5, columns=1, sticky="w", padx=20, pady=10)

        añolabel = tk.Label(marco, text="Año: ", bg=colormarco, fg=colorletra, font=("arial",11))
        añolabel.grid(row=6, columns=1, sticky="W", padx=20, pady=10)

        registrarAtencionBoton = tk.Button(marco, text="Registrar Atencion al emprendedor", command=self.registrarAtencion, bg=colorboton, fg=colorletraboton)
        registrarAtencionBoton.grid(row=7, columnspan=1, sticky="w", padx=120, pady=5)

    def registrarAtencion(self):
        messagebox.showinfo("registro de atencion al emprendedor, registrado", message)



if __name__ == "__main__":
    root = tk.Tk()
    app = AtencionesEmprendedor(root)
    root.mainloop()

    