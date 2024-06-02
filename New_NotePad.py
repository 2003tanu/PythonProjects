import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os

def createWidgets():
    global textArea
    textArea = Text(root)
    textArea.grid(sticky=N+E+S+W)

    menuBar = Menu(root)
    root.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exitApp)
    menuBar.add_cascade(label="File", menu=fileMenu)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=help)
    menuBar.add_cascade(label="Help", menu=helpMenu)

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text documents", "*.txt")])
    if file:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        with open(file, "r") as file_obj:
            textArea.insert(1.0, file_obj.read())

def saveFile():
    global file
    if not file:
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text documents", "*.txt")])
        if not file:
            return
    with open(file, "w") as file_obj:
        file_obj.write(textArea.get(1.0, END))
    root.title(os.path.basename(file) + " - Notepad")

def exitApp():
    root.destroy()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def help():
    messagebox.showinfo("Notepad", "This is a simple Notepad application created using Tkinter.")

root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")
file = None

createWidgets()

root.mainloop()
