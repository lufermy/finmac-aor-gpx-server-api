from tkinter import *
from tkinter.ttk import *
import sys

master = Tk()
 
master.geometry("250x100")
master.title("Coords2GPX")
master.iconbitmap(sys.executable)

def startServer():
    startServerButton.place_forget()
    stopServerButton.place(x=5,y=40)
    serverStatusLabel=Label(master, text ="Servidor iniciado.", foreground='#00FF00')
    serverStatusLabel.place_forget()
    serverStatusLabel.place(x=5,y=70)
def stopServer():
    stopServerButton.place_forget()
    startServerButton.place(x=5,y=40)
    serverStatusLabel = Label(master, text ="Servidor detenido.", foreground='#FF0000')
    serverStatusLabel.place_forget()
    serverStatusLabel.place(x=5,y=70)
# ENTRIES
portEntry = Entry()
portEntry.insert(0, "8080")
portEntry.place(x=55,y=10)

#LABELS
portEntryLabel = Label(master, text="Puerto: ")
portEntryLabel.place(x=5,y=10)
serverStatusLabel = Label(master, text ="Servidor detenido.", foreground='#FF0000')
serverStatusLabel.place(x=5,y=70)

#BUTTONS
startServerButton = Button(master, text ="Iniciar", command = startServer)
stopServerButton = Button(master, text ="Detener", command = stopServer)
startServerButton.place(x=5,y=40)
 

mainloop()