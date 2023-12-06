import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from conexion import Conexion


class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('450x400+100+100')
        self.title('Libreria')
        self.conn = Conexion()
        self.conn.conexion_base()
        self._crear_tabs()

    def tabulador1(self, tabulador):
        # etiqueta y un componente de entrada

        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        #self.isbn = 
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

        etiqueta6 = ttk.Label(tabulador, text='Fecha de inicio(DD/MM/AA): ')
        etiqueta6.grid(row=5, column=0, sticky=tk.E)
        entrada6 = ttk.Entry(tabulador, width=30)
        entrada6.grid(row=5, column=1, padx=5, pady=5)

        etiqueta7 = ttk.Label(tabulador, text='Fecha de fin(DD/MM/AA): ')
        etiqueta7.grid(row=6, column=0, sticky=tk.E)
        entrada7 = ttk.Entry(tabulador, width=30)
        entrada7.grid(row=6, column=1, padx=5, pady=5)


        # botón para registrar
        def enviar():
            isbn = entrada1.get()
            titulo = entrada2.get()
            nombre_editorial = entrada3.get()
            anio_libro = entrada4.get()
            nombre_autor = entrada5.get()
            fecha_ini = entrada6.get()
            fecha_fin = entrada7.get()

            self.conn.insertar_libro(isbn,titulo,nombre_editorial,anio_libro,nombre_autor,fecha_ini,fecha_fin)

            messagebox.showinfo('Mensaje', f'Libro registrado correctamente.')

        boton1 = ttk.Button(tabulador, text='OK', command = enviar)
        boton1.grid(row=8, column=0, columnspan=2)

    def tabulador2(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # botón para mostrar la fecha seleccionada
        def buscar_valor():
            isbn_buscar = entrada1.get()
            records = self.conn.buscar_libro_por_isbn(isbn_buscar)

            if records:
                mensaje = "Libro encontrado:\n"
                for row in records:
                    mensaje += f"ISBN: {row[0]}\nTítulo: {row[1]}\nEditorial: {row[2]}\nAño: {row[3]}\nAutor: {row[4]}\n"
                messagebox.showinfo('Busqueda', mensaje)
            else:
                messagebox.showinfo("Resultado de la búsqueda", "Libro no encontrado.")

        boton_mostrar = ttk.Button(tabulador, text='OK', command = buscar_valor)
        boton_mostrar.grid(row=3, column=1)

    def tabulador3(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='ISBN del libro:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        etiqueta2 = ttk.Label(tabulador, text='Titulo del libro a modificar:')
        etiqueta2.grid(row=1, column=0, sticky=tk.E)
        entrada2 = ttk.Entry(tabulador, width=30)
        entrada2.grid(row=1, column=1, padx=5, pady=5)

        # botón para mostrar la fecha seleccionada
        def actualizar_valor():
            buscar_isbn = entrada1.get()
            nombre_libro = entrada2.get()

            self.conn.actualizar_titulo(nombre_libro,buscar_isbn)

            messagebox.showinfo('Actualización', f'Actualización completada')

        boton_mostrar = ttk.Button(tabulador, text='OK', command = actualizar_valor)
        boton_mostrar.grid(row=3, column=1)

    def tabulador4(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='ISBN del libro a eliminar:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # botón para mostrar la fecha seleccionada
        def eliminar_valor():
            eliminar_libro = entrada1.get()
        
            self.conn.eliminar_libro(eliminar_libro)

            messagebox.showinfo('Eliminación', 'Eliminación completada')

        boton_mostrar = ttk.Button(tabulador, text='OK', command = eliminar_valor)
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

        # tabulador 3
        # Update, con el titulo actualizar

        tabulador3 = ttk.LabelFrame(control_tabulador, text='Actualizar')
        control_tabulador.add(tabulador3, text='ISBN a actualizar')
        self.tabulador3(tabulador3)

        # tabulador 5
        # borrar, con el ISBN
        tabulador4 = ttk.LabelFrame(control_tabulador, text='Borrar')
        control_tabulador.add(tabulador4, text='Borrar')
        self.tabulador4(tabulador4)

    """ def Agregar(self):
            entrada1 = ttk.Entry(entrada1.get())
            entrada2 = ttk.Entry(entrada2.get())
            entrada3 = ttk.Entry(entrada2.get())
            entrada4 = ttk.Entry(entrada2.get())
            entrada5 = ttk.Entry(entrada2.get()) """

if __name__ == '__main__':
    # Creamos un objeto de nuestra clase
    componentes_ventana = ComponentesVentana()
    componentes_ventana.mainloop()   


