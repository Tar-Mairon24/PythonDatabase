import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta


class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('350x300+200+200')
        self.title('Libreria')

        self._crear_tabs()

    def tabulador1(self, tabulador):
        # etiqueta y un componente de entrada

        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        etiqueta2 = ttk.Label(tabulador, text='Titulo:')
        etiqueta2.grid(row=1, column=0, sticky=tk.E)
        entrada2 = ttk.Entry(tabulador, width=30)
        entrada2.grid(row=1, column=1, padx=5, pady=5)

        etiqueta3 = ttk.Label(tabulador, text='Editorial:')
        etiqueta3.grid(row=2, column=0, sticky=tk.E)
        entrada3 = ttk.Entry(tabulador, width=30)
        entrada3.grid(row=2, column=1, padx=5, pady=5)

        etiqueta4 = ttk.Label(tabulador, text='Año:')
        etiqueta4.grid(row=3, column=0, sticky=tk.E)
        entrada4 = ttk.Entry(tabulador, width=30)
        entrada4.grid(row=3, column=1, padx=5, pady=5)

        etiqueta5 = ttk.Label(tabulador, text='Autor:')
        etiqueta5.grid(row=4, column=0, sticky=tk.E)
        entrada5 = ttk.Entry(tabulador, width=30)
        entrada5.grid(row=4, column=1, padx=5, pady=5)

        etiqueta6 = ttk.Label(tabulador, text='Fecha de inicio:')
        etiqueta6.grid(row=5, column=0, sticky=tk.E)
        fecha_actual = datetime.now()
        fecha_ini = [fecha_actual - timedelta(days=x) for x in range(30)]
        fecha_ini_str = [fecha.strftime("%Y-%m-%d") for fecha in fecha_ini]

        etiqueta7 = ttk.Label(tabulador, text='Fecha de fin:')
        etiqueta7.grid(row=6, column=0, sticky=tk.E)
        fecha_actual = datetime.now()
        fecha_fin = [fecha_actual - timedelta(days=x) for x in range(30)]
        fecha_fin_str = [fecha.strftime("%Y-%m-%d") for fecha in fecha_fin]

        # Combobox con las fechas
        combobox = ttk.Combobox(tabulador, width=30, values=fecha_ini_str)
        combobox.grid(row=5, column=1, padx=5, pady=5)

        combobox = ttk.Combobox(tabulador, width=30, values=fecha_fin_str)
        combobox.grid(row=6, column=1, padx=5, pady=5)

        # Seleccionamos la primera fecha pasada como predeterminada
        combobox.current(0)

        # botón para registrar
        def enviar():
            messagebox.showinfo('Mensaje', f'Libro registrado correctamente.')

        boton1 = ttk.Button(tabulador, text='OK', command=enviar)
        boton1.grid(row=7, column=0, columnspan=2)

    def tabulador2(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # botón para mostrar la fecha seleccionada
        def mostrar_valor():
            messagebox.showinfo('Memo Joto', 'Registro completado')

        boton_mostrar = ttk.Button(tabulador, text='OK', command=mostrar_valor)
        boton_mostrar.grid(row=3, column=1)

    def _crear_tabs(self):
        # Creamos un tab control, para ello usamos la clase Notebook
        control_tabulador = ttk.Notebook(self)
        # Agregamos un marco (frame) para agregar dentrol del tab y organizar elementos
        tabulador1 = ttk.Frame(control_tabulador)
        # Agregamos el tabulador al control de tabuladores
        control_tabulador.add(tabulador1, text='Ingresar Libro')
        # Mostramos el tabulador
        control_tabulador.pack(fill='both')
        # Creamos los componentes del tabulador1
        self.tabulador1(tabulador1)

        tabulador2 = ttk.LabelFrame(control_tabulador, text='Busqueda de libro')
        control_tabulador.add(tabulador2, text='Busqueda de libro')
        self.tabulador2(tabulador2)


if __name__ == '__main__':
    # Creamos un objeto de nuestra clase
    componentes_ventana = ComponentesVentana()
    componentes_ventana.mainloop()