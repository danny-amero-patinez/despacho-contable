import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk, Image
class ModificarEmprendedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Modificar informarcion del emprendedor")
        self.editing = False

        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        ancho_ventana = 700
        alto_ventana = 400

        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        colormarco = "#009688"
        colorletra = "#ffffff"
        colorboton = "#607d8b"
        colorletraboton = "#000000"

        self.root.configure(bg=colormarco)

        marco = tk.Frame(root, bd=5, bg=colormarco)
        marco.pack(expand=True, fill="both")

        titulolabel = tk.Label(marco, text="Modificar informacion del emprendedor", bg=colormarco, fg=colorletra, font=("Helvetica", 16))
        titulolabel.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        select_label = ttk.Label(marco, text="Selecciona al Emprendedor:", background=colormarco, foreground=colorletra)
        select_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Lista desplegable para seleccionar al cliente
        self.emprendedor_nombre = []  # Lista para almacenar nombres de clientes

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='lion',
                                                 user='root',
                                                 password='panconl3ch3.')

            sql_select_Query = "select NombreProyecto from emprendedores"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            # query = ""
            self.emprendedor_nombre = [x for x in records]

        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Error reading data from MySQL table.")
            # print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                # print("MySQL connection is closed")

        self.seleccion_emprendedor = tk.StringVar()
        self.emprendedor_dropdown = ttk.Combobox(marco, textvariable=self.seleccion_emprendedor, values=self.emprendedor_nombre)
        self.emprendedor_dropdown.grid(row=2, column=1, padx=10, pady=5)

        # Botón para cargar la información del cliente seleccionado
   #     load_button = ttk.Button(marco, text="Cargar Información", command=self.load_client_info, style="TButton")
   #     load_button.grid(row=1, column=2, padx=10, pady=5)

        # Campos de entrada para editar la información del cliente
        nombre_label = ttk.Label(marco, text="Nombre:", background=colormarco, foreground=colorletra)
        nombre_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.nombre_entry = ttk.Entry(marco)
        self.nombre_entry.grid(row=3, column=1, padx=10, pady=5)

        apellido_label = ttk.Label(marco, text="Apellido:", background=colormarco, foreground=colorletra)
        apellido_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.apellido_entry = ttk.Entry(marco)
        self.apellido_entry.grid(row=4, column=1, padx=10, pady=5)

        direccion_label = ttk.Label(marco, text="Dirección:", background=colormarco, foreground=colorletra)
        direccion_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.direccion_entry = ttk.Entry(marco)
        self.direccion_entry.grid(row=5, column=1, padx=10, pady=5)

        regimen_label = ttk.Label(marco, text="Régimen Fiscal:", background=colormarco, foreground=colorletra)
        regimen_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.regimen_entry = ttk.Entry(marco)
        self.regimen_entry.grid(row=6, column=1, padx=10, pady=5)

        # Botón para aplicar los cambios y guardar la información del cliente
        save_button = ttk.Button(marco, text="Guardar Cambios", command=self.modificarEmprendedor, style="TButton")
        save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        cargar_info = ttk.Button(marco, text="Cargar Informacion", command=self.cargarInformacion, style="TButton")
        cargar_info.grid(row=1, column=2, padx=10, pady=5)

        # Deshabilitar la edición de los campos por defecto
    #    self.toggle_editing()

        self.toggle_editing()

    def toggle_editing(self):
        # Alternar entre modo de edición y vista
        state = tk.NORMAL if self.editing else tk.DISABLED
        self.nombre_entry.config(state=state)
        self.apellido_entry.config(state=state)
        self.direccion_entry.config(state=state)
        self.regimen_entry.config(state=state)

    def modificarEmprendedor(self):
        # Agregar aquí la lógica para guardar los cambios en la información del cliente
        # en tu base de datos o sistema de almacenamiento
        tk.messagebox.showinfo("Guardar Cambios", "Cambios guardados exitosamente")
        self.toggle_editing()  # Deshabilitar la edición

    def cargarInformacion(self):
        seleccion_emprendedor = self.seleccion_emprendedor.get()
        data = ""
        if seleccion_emprendedor:
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='lion',
                                                     user='root',
                                                     password='panconl3ch3.')

                sql_select_Query = "select * from emprendedores where NombreProyecto = %s"

                cursor = connection.cursor()
                cursor.execute(sql_select_Query, (seleccion_emprendedor,))
                data = cursor.fetchall()

            except mysql.connector.Error as e:
                messagebox.showerror("Error", "Error reading data from MySQL table.")
                # print("Error reading data from MySQL table", e)
            finally:
                if connection.is_connected():
                    connection.close()
                    cursor.close()
                    # print("MySQL connection is closed")

            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, data[0][8])
            self.apellido_entry.delete(0, tk.END)
            self.apellido_entry.insert(0, data[0][13])
            self.direccion_entry.delete(0, tk.END)
            self.direccion_entry.insert(0, data[0][12])
            self.regimen_entry.delete(0, tk.END)
            self.regimen_entry.insert(0, data[0][11])
        else:
            messagebox.showwarning("Advertencia", "Selecciona un cliente antes de cargar la información.")




if __name__ == "__main__":
    root = tk.Tk()
    app = ModificarEmprendedor(root)
    root.mainloop()
