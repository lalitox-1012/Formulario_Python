# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:54:50 2024

@author: Eduardo Castillejos
"""

import tkinter as tk
from tkinter import messagebox

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)
    
def borrar_fun():
    limpiar_campos()

def guardar_valores():
    nombres = tbNombre.get()
    apellidos = tbApellido.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
        
    datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad} años\nEstatura: {estatura}\nTelefono: {telefono}\nGenero: {genero}\n"

    with open("FormularioDatos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
    
    messagebox.showinfo("Informacion", "Datos guardados exitosamente: \n\n" + datos)
    limpiar_campos()

ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Datos")

var_genero = tk.IntVar()

lbNombre = tk.Label(ventana, text="Nombres: ")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()
lbApellido = tk.Label(ventana, text="Apellidos: ")
lbApellido.pack()
tbApellido = tk.Entry(ventana)
tbApellido.pack()
lbTelefono = tk.Label(ventana, text="Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()
lbEdad = tk.Label(ventana, text="Edad: ")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()
lbEstatura = tk.Label(ventana, text="Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()
lbGenero = tk.Label(ventana, text="Genero: ")
lbGenero.pack()
rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()