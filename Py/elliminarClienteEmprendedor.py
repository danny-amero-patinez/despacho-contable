import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

cliente = []
emprendedor = []

class eliminarClienteEmprendedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Elminar cliente o emprendedor")

        anchoPantalla = root.winfo_screenwidth()
        altoPantalla = root.winfo_screenheight()

        anchoVentana = 550
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

        atencionesLabel = tk.Label(marco, text="Eliminar cliente o emprendedor", bg=colormarco, fg=colorletra, font=("arial", 14))
        atencionesLabel.grid(row=1, columns=1, sticky="w", padx=80, pady=10)

        elimCliente = tk.Label(marco, text="Eliminar Cliente", bg=colormarco, fg=colorletra, font=("arial",11))
        elimCliente.grid(row=5, columns=1, sticky="w", padx=50, pady=10)

        elimEmprendedor = tk.Label(marco, text="Eliminar Emprendedor", bg=colormarco, fg=colorletra, font=("arial",11))
        elimEmprendedor.grid(row=5, columns=1, sticky="w", padx=280, pady=10)

        self.eliminarClientecombobox = ttk.Combobox(marco, values=cliente, font=("arial", 11))
        self.eliminarClientecombobox.grid(row=300, column=0,  pady=20, sticky="w", padx=10)

        self.eliminarEmprendedorcombobox = ttk.Combobox(marco, values=emprendedor , font=("arial", 11))
        self.eliminarEmprendedorcombobox.grid(row=300, column=0, pady=20, sticky="w", padx=270)

        eliminarcliente = tk.Button(marco, text="Eliminar cliente", command=self.eliminar_Cliente, bg=colorboton, fg=colorletraboton, font=("arial",11))
        eliminarcliente.grid(row=100, padx=40, columnspan=1, sticky="w", pady=10)

        eliminaremprendedor = tk.Button(marco, text="Eliminar emprendedor", command=self.eliminar_Emprendedor, bg=colorboton, fg=colorletraboton, font=("arial",11))
        eliminaremprendedor.grid(row=100, padx=285, columnspan=1, sticky="w", pady=10)


    def eliminar_Cliente(self):                                      
        messagebox.showinfo(title="Eliminar clienter", message="Se elimino al cliete seleccionado")
        

    def eliminar_Emprendedor(self):
        messagebox.showinfo(title="Eliminar emprendedor", message="Se elimino al emprendedor seleccionado")



if __name__ == "__main__":
    root = tk.Tk()
    app = eliminarClienteEmprendedor(root)
    root.mainloop()