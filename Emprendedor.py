import tkinter as tk

class Emprendedor:
     def __init__(self, root):
        self.root = root
        self.root.title("Pantalla Emprendedor")

        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        ancho_ventana = 700
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

      #  letraLabel = Font(family="arial", size=14)
      #  letraLabel2 = Font(family="arial", size=12)
      #  letraLabel3 = Font(family="arial", size=11)

        tituloLabel = tk.Label(marco, text="Informacion Emprendedor", bg=colorMarco, fg=colorLabel, font=("arial",11))
        tituloLabel.grid(row=0, column=1, sticky="w",pady=5, ipadx=70)

        idLabel = tk.Label(marco, text="ID Cliente", bg=colorMarco, fg=colorLabel, font=("arial",11))
        idLabel.grid(row=1, column=1, sticky="w",pady=5, ipadx=70)

        nombreLabel = tk.Label(marco, text="Nombre", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nombreLabel.grid(row=2, column=1, sticky="w",pady=5, ipadx=70)

        negocioLabel = tk.Label(marco, text="Nombre del negocio", bg=colorMarco, fg=colorLabel, font=("arial",11))
        negocioLabel.grid(row=3, column=1, sticky="w",pady=5, ipadx=70)

        correoLabel = tk.Label(marco, text="Correo", bg=colorMarco, fg=colorLabel, font=("arial",11))
        correoLabel.grid(row=4, column=1, sticky="w",pady=5, ipadx=70)

        rfcLabel = tk.Label(marco, text="RFC", bg=colorMarco, fg=colorLabel, font=("arial",11))
        rfcLabel.grid(row=5, column=1, sticky="w",pady=5, ipadx=70)

        nssLabel = tk.Label(marco, text="NSS", bg=colorMarco, fg=colorLabel, font=("arial",11))
        nssLabel.grid(row=6, column=1, sticky="w",pady=5, ipadx=70)

        postalLabel = tk.Label(marco, text="Codigo Postal", bg=colorMarco, fg=colorLabel, font=("arial",11))
        postalLabel.grid(row=7, column=1, sticky="w",pady=5, ipadx=70)

        capitalLabel = tk.Label(marco, text="Capiatal inicial", bg=colorMarco, fg=colorLabel, font=("arial",11))
        capitalLabel.grid(row=8, column=1, sticky="w",pady=5, ipadx=70)

        tipoPersonaLabel = tk.Label(marco, text="Tipo de Persona", bg=colorMarco, fg=colorLabel, font=("arial",11))
        tipoPersonaLabel.grid(row=9, column=1, sticky="w", pady=5, ipadx=70)

        tipoPersonaLabel = tk.Label(marco, text="Observaciones", bg=colorMarco, fg=colorLabel, font=("arial",11))
        tipoPersonaLabel.grid(row=9, column=1, sticky="w", pady=5, ipadx=70)

      def abrir(self):
        conexion = msql.connector.connect(
            host='localhost',
            user='root',
            database='<lion>',
            password='<julianms3>'
            )

        return conexion

      def consulta(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select idcliente, NombresCompletos Correo1, CapitalInicial, RFC, NSS, Direccion, Observaciones regimen from emprendedores"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
