from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
import os
# Weidth and height
WEIDTH = 400
HEIGHT = 400

def NewFile():
    pass

def OpenFile():
    pass

def SaveFile():
    pass

def ExitFile():
    pass 

def CutFile():
    pass

def CopyFile():
    pass

def PasteFile():
    pass

def About():
    pass


if __name__ == "__main__":
    # Basic window Setup
    root = Tk()
    root.geometry(f"{WEIDTH}x{HEIGHT}")
    root.title("Untitled-Notepad ")

    # Adding textares
    TextArea = Text(root, font="lucida 13")
    file = None 
    TextArea.pack(expand=True, fill=BOTH)

    # Creating Menubar
    Menubar = Menu(root)

    # creating file menu
    FileMenu = Menu(Menubar, tearoff=0)
        # to give features of New, save, open to Filemenu
    FileMenu.add_command(label="New", command=NewFile)
    FileMenu.add_command(label="Save", command= SaveFile)
    FileMenu.add_command(label="Open", command=OpenFile)
        # Adding Seperator
    FileMenu.add_separator()
        # Adding Exit command
    FileMenu.add_command(label="Exit", command= ExitFile)
    Menubar.add_cascade(label="File", menu=FileMenu)

    # creating Edit menu
    EditMenu = Menu(Menubar, tearoff=0)
        # to give features of Cut, Copy, Paste to Filemenu
    EditMenu.add_command(label="Cut", command= CutFile)
    EditMenu.add_command(label="Copy", command= CopyFile)
    EditMenu.add_command(label="Paste", command= PasteFile)
    Menubar.add_cascade(label="Edit", menu=EditMenu)

    # Creating Help menu
    HelpMenu = Menu(Menubar, tearoff =0)
        # Add about menu
    HelpMenu.add_command(label="About", command= About)
    Menubar.add_cascade(label="Help", menu=HelpMenu)

    Menubar.config(menu=Menubar)
    
    
    root.mainloop()
