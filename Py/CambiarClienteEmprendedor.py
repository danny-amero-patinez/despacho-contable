import tkinter as tk

class Cambiarcliente:
    def __init__(self, root):
        self.root = root
        self.root.title("Cambiar de cliente a emprendedor")

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

        clienteLabel = tk.Label(marco, text="Cliente", bg=colorMarco, fg=colorLabel)
        clienteLabel.grid(row=1, column=0, sticky="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = Cambiarcliente(root)
    root.mainloop()