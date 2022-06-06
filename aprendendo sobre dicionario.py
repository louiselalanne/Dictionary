from tkinter import *
import tkinter
root = Tk()
root.title("Dictionary")
root.geometry("600x400")

label_mutable = Label(root)
label_immutable = Label(root)
label_tkinter = Label(root)

dictionary = {'Mutável' : 'Valores podem ser alterados como em uma lista',
            'Imutável' : 'Valores não podem ser alterados como as tuplas',
            'Tkinter' : 'É a bibliotera GUI de python'}

def mutable():
    label_mutable["text"] = dictionary['Mutável']

def immutable():
    label_immutable["text"] = dictionary['Imutável']

def tkintere():
    label_tkinter["text"] = dictionary['Tkinter']

btn_mut = Button(root, text="Significado de Mutável", command=mutable)
btn_mut.place(relx=0.5, rely=0.2, anchor=CENTER)

btn_immut = Button(root, text="Significado de Imutável", command=immutable)
btn_immut.place(relx=0.5, rely=0.4, anchor=CENTER)

btn_tkinter = Button(root, text="Significado de Tkinter", command=tkintere)
btn_tkinter.place(relx=0.5, rely=0.6, anchor=CENTER)

label_mutable.place(relx=0.5, rely=0.3, anchor=CENTER)
label_immutable.place(relx=0.5, rely=0.5, anchor=CENTER)
label_tkinter.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()