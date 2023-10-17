import tkinter as tk
from tkinter import messagebox


class AdminLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión del Administrador")

        # Obtiene el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana en la pantalla
        window_width = 400
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Establece la geometría de la ventana

        # Colores personalizados de la paleta
        frame_color = "#009688"  # VERDE PRIMARIO
        label_color = "#FFFFFF"  # GRIS
        button_color = "#607D8B"  # GRIS OSCURO
        button_text_color = "#FFFFFF"  # VERDE OSCURO

        # Configura el fondo de la ventana principal con el color deseado
        self.root.configure(bg=frame_color)

        # Crear un marco transparente para organizar los elementos
        frame = tk.Frame(root, bg=frame_color, bd=5)
        frame.grid(row=0, column=0, sticky="nsew")  # Utilizar grid para ocupar toda la celda

        # Configurar las columnas y filas para hacer que la interfaz sea responsiva
        root.columnconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)

        # Etiqueta de título
        title_label = tk.Label(frame, text="Despacho Contable", font=("Helvetica", 20), bg=frame_color, fg=label_color)
        title_label.grid(row=0, column=0, columnspan=2, pady=20)  # Alineación arriba

        # Etiqueta de nombre de usuario
        username_label = tk.Label(frame, text="Usuario", font=("Helvetica", 12), bg=frame_color,
                                  fg=label_color)
        username_label.grid(row=1, column=0, pady=10)  # Alineación arriba

        # Campo de entrada de nombre de usuario
        self.username_entry = tk.Entry(frame, font=("Helvetica", 12))
        self.username_entry.grid(row=2, column=0, pady=10, padx=10, columnspan=2, sticky="ew")  # Span de columnas

        # Etiqueta de contraseña
        password_label = tk.Label(frame, text="Contraseña", font=("Helvetica", 12), bg=frame_color, fg=label_color)
        password_label.grid(row=3, column=0, pady=10)  # Alineación arriba

        # Campo de entrada de contraseña
        self.password_entry = tk.Entry(frame, show="*", font=("Helvetica", 12))
        self.password_entry.grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky="ew")  # Span de columnas

        # Botón de inicio de sesión del administrador
        admin_login_button = tk.Button(frame, text="Iniciar Sesión", command=self.attempt_admin_login,
                                       font=("Helvetica", 14), bg=button_color, fg=button_text_color)
        admin_login_button.grid(row=5, column=0, columnspan=2, pady=20)  # Alineación arriba

    def attempt_admin_login(self):
        # Simulación de la comprobación de credenciales del administrador
        admin_username = self.username_entry.get()
        admin_password = self.password_entry.get()

        # Verificar las credenciales
        if admin_username == "admin" and admin_password == "admin123":
            # Si las credenciales son correctas, realizar las acciones de inicio de sesión del administrador
            messagebox.showinfo("Éxito", "Inicio de sesión del administrador exitoso")
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

    def abrir_pagina_principal_admin(self):
        # Cerrar la ventana actual
        self.root.destroy()

        # Crear una nueva ventana para la página principal
        root = tk.Tk()
        from PrincipalAdmin import principalAdmin
        principalAdmin(root)
        root.mainloop()

    if __name__ == "__main__":
        root = tk.Tk()
        app = principalAdmin(root)
        root.mainloop()
