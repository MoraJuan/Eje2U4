
from tkinter import *
from tkinter import ttk, messagebox, font
import tkinter as tk


class Aplicacion(tk.Tk):
    __ventana=None
    __siniva=None
    __iva=None
    __precioIVA=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x300')
        self.__ventana.title('Conversor IVA')
        fuente=font.Font(font='Verdana 10',weight='normal')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__siniva = StringVar()
        self.__iva = StringVar()
        self.__precioIVA = StringVar()

        #self.__siniva.trace('w', self.calcular)
        self.sinivaEntry = ttk.Entry(mainframe, width=7, textvariable=self.__siniva)
        self.sinivaEntry.grid(column=2, row=1, sticky=(W, E))
       

        ttk.Radiobutton(mainframe, text='IVA 21%', value=0).grid(row =2, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(mainframe, text='IVA 10.5%', value=1).grid(row =3, column=0, columnspan=1,sticky='w')
        ttk.Label(mainframe, textvariable=self.__precioIVA).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="Precio sin IVA").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="centímetros").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        #self.pulgadasEntry.focus()
        self.__ventana.mainloop()

def testAPP():
    mi_app = Aplicacion()



if __name__ == '__main__':
    testAPP()
