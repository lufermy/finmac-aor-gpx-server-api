from tkinter import *
from tkinter.ttk import *
import sys
import json

#DATA LOADING
settingsfile = open('./settings.json')
settingsdata = json.load(settingsfile)
settings_username = settingsdata["username"]
settings_servername = settingsdata["servername"]
settings_database = settingsdata["database"]
settings_defaultport = settingsdata["defaultport"]
settingsfile.close()



root=Tk()
root.geometry("250x100")
root.title("Coords2GPX")
root.iconbitmap(sys.executable)

def startServer():
    startServerButton.place_forget()
    stopServerButton.place(x=5,y=40)
    serverStatusLabel=Label(root, text ="Servidor iniciado.", foreground='#00FF00')
    serverStatusLabel.place_forget()
    serverStatusLabel.place(x=5,y=70)
def stopServer():
    stopServerButton.place_forget()
    startServerButton.place(x=5,y=40)
    serverStatusLabel = Label(root, text ="Servidor detenido.", foreground='#FF0000')
    serverStatusLabel.place_forget()
    serverStatusLabel.place(x=5,y=70)
# ENTRIES
portEntry = Entry()
portEntry.insert(0, str(settings_defaultport))
portEntry.place(x=55,y=10)

#LABELS
portEntryLabel = Label(root, text="Puerto: ")
portEntryLabel.place(x=5,y=10)
serverStatusLabel = Label(root, text ="Servidor detenido.", foreground='#FF0000')
serverStatusLabel.place(x=5,y=70)

#BUTTONS
startServerButton = Button(root, text ="Iniciar", command = startServer)
stopServerButton = Button(root, text ="Detener", command = stopServer)
startServerButton.place(x=5,y=40)


mainloop()