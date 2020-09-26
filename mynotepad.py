from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
import os
# Weidth and height
WEIDTH = 400
HEIGHT = 400

def NewFile():
    global file 
    root.title('Galvic-Notepad')
    file = None 
    TextArea.delete(1.0, END)

def OpenFile():
    global file 
    file = askopenfilename(defaultextension='.txt',
                            filetypes= [("All files", "*.*"),
                            ("Text Documents", "*.txt*")                                
                            ])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ " -Notepad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()



def SaveFile():
        global file
        if file == None:
            file = askopenfilename(initialfile= "untitled.txt", defaultextension= ".txt",
                                    filetypes= [("All Files", "*.*"),
                                    ("Text Documents", "*.txt*")])
            if file == "":
                file = None 
            else:
                # saving as a new file 
                f = open(file, 'w')
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file)+ " -Notepad")
                print("File Saved Successfully!")

        else:
            # save the file 
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

def ExitFile():
    root.destroy()

def CutFile():
    TextArea.event_generate("<<Cut>>")

def CopyFile():
    TextArea.event_generate("<<Copy>>")

def PasteFile():
    TextArea.event_generate("<<Paste>>")

def About():
    showinfo(title="GALVIC-NOTEPAD", message="""welcome to Galvic's notepad,\n
                         you can use basic functionalities of notepad here!.\n
                         Thankyu for using my Notepad.\n
                                          - Himanshu Sharma (creator) """) 


if __name__ == "__main__":
    # Basic window Setup
    root = Tk()
    root.geometry(f"{WEIDTH}x{HEIGHT}")
    root.title("Galvic-Notepad ")
    
    # Adding textares
    TextArea = Text(root, font="lucida 13", fg="white")
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

    root.config(menu=Menubar)
    TextArea.config(bg='black')

    # Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
    root.mainloop()
