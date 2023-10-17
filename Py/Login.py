import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Iniciar Sesión")

        fuente_personalizada = tkfont.Font(family="Work Sans", size=12)

        # Obtiene el ancho y alto de la pantalla
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana en la pantalla
        ancho_ventana = 400
        alto_ventana = 400
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")  # Establece la geometría de la ventana

        # Colores personalizados de la paleta
        color_marco = "#009688"  # VERDE PRIMARIO
        color_etiqueta = "#FFFFFF"  # GRIS
        color_boton = "#607D8B"  # GRIS OSCURO
        color_texto_boton = "#FFFFFF"  # VERDE OSCURO

        # Configura el fondo de la ventana principal con el color deseado
        self.root.configure(bg=color_marco)

        # Crear un marco transparente para organizar los elementos
        marco = tk.Frame(root, bg=color_marco, bd=5)
        marco.grid(row=0, column=0, sticky="nsew")  # Utilizar grid para ocupar toda la celda

        # Configurar las columnas y filas para hacer que la interfaz sea responsiva
        root.columnconfigure(0, weight=1)
        marco.columnconfigure(0, weight=1)
        marco.columnconfigure(1, weight=1)
        marco.columnconfigure(2, weight=1)
        marco.columnconfigure(3, weight=1)
        marco.rowconfigure(0, weight=1)
        marco.rowconfigure(1, weight=1)
        marco.rowconfigure(2, weight=1)
        marco.rowconfigure(3, weight=1)
        marco.rowconfigure(4, weight=1)

        # Etiqueta de título
        etiqueta_titulo = tk.Label(marco, text="Despacho Contable", font=fuente_personalizada, fg=color_etiqueta,
                                   bg=color_marco)
        etiqueta_titulo.grid(row=0, column=0, columnspan=4, pady=(20, 0))  # Alineación arriba, span de columnas

        # Etiqueta de nombre de usuario
        etiqueta_usuario = tk.Label(marco, text="Usuario", font=fuente_personalizada, bg=color_marco, fg=color_etiqueta)
        etiqueta_usuario.grid(row=1, column=0, pady=(20, 10))  # Alineación arriba

        # Campo de entrada de nombre de usuario
        self.entrada_usuario = tk.Entry(marco, font=fuente_personalizada)
        self.entrada_usuario.grid(row=2, column=0, pady=10, padx=10, columnspan=4, sticky="ew")  # Span de columnas

        # Etiqueta de contraseña
        etiqueta_contrasena = tk.Label(marco, text="Contraseña", font=fuente_personalizada, bg=color_marco,
                                       fg=color_etiqueta)
        etiqueta_contrasena.grid(row=3, column=0, pady=10)  # Alineación arriba

        # Campo de entrada de contraseña
        self.entrada_contrasena = tk.Entry(marco, show="*", font=fuente_personalizada)
        self.entrada_contrasena.grid(row=4, column=0, pady=10, padx=10, columnspan=4, sticky="ew")  # Span de columnas

        # Botón de inicio de sesión
        boton_inicio_sesion = tk.Button(marco, text="Iniciar Sesión", command=self.intentar_inicio_sesion,
                                        font=fuente_personalizada,
                                        bg=color_boton, fg=color_texto_boton)
        boton_inicio_sesion.grid(row=5, column=0, columnspan=4, pady=20)  # Alineación arriba, span de columnas

        boton_inicio_admin = tk.Button(marco, text="Iniciar Sesión como Administrador",
                                       command=self.abrir_inicio_sesion_admin,
                                       font=fuente_personalizada, bg=color_boton, fg=color_texto_boton)
        boton_inicio_admin.grid(row=6, column=0, columnspan=4, pady=10)  # Añadir el botón arriba

    def abrir_inicio_sesion_admin(self):
        # Cerrar la ventana actual
        self.root.destroy()

        # Crear una nueva ventana para la página de inicio de sesión del administrador
        ventana_admin = tk.Tk()
        from LoginAdmin import AdminLoginApp
        AdminLoginApp(ventana_admin)
        ventana_admin.mainloop()

    def intentar_inicio_sesion(self):
        # Simulación de la comprobación de credenciales
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()

        # Verificar las credenciales
        if usuario == "ivan" and contrasena == "1234":
            # Si las credenciales son correctas, abrir la ventana principal
            self.abrir_pagina_principal()
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

    def abrir_pagina_principal(self):
        # Cerrar la ventana actual
        self.root.destroy()

        # Crear una nueva ventana para la página principal
        root = tk.Tk()
        from Principal import HomeApp
        HomeApp(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()