from tkinter import *
# global weidth and height
WIN_WIDTH = 580
WIN_HEIGHT = 450

def NewFile():
    pass

def OpenFile():
    pass

def SaveFile():
    pass

def ExitFile():
    pass

def Cut():
    pass

def Copy():
    pass

def Paste():
    pass

def About():
    pass



# main setup
if __name__ == "__main__":
    # basic tkinter setup
    root = Tk()
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
    root.title("Untitled - Notepad")

    # adding text area
    textarea = Text(root, font = "lucida 13")
    file = none
    textarea.pack(expand = True, fill= BOTH)

    # creating the menubar
    MenuBar = Menu(root)

    # creating file menu
    FileMenu = Menu(MenuBar, tearoff = 0) 
        # to open a new file 
    FileMenu.add_command(name="New", command= NewFile)
        # to open a pre-existing file
    FileMenu.add_command(name="Opem", command= OpenFile)
        # to save a file 
    FileMenu.add_command(name= "save",command= SaveFile)
    FileMenu.add_separator()
    FileMenu.add_command(name= "Exit", command= ExitFile)
    MenuBar.add_cascade(name="File", menu= FileMenu )         

    # creating edit menu
    EditMenu = Menu(MenuBar, tearoff = 0)
        # to cut , copy, paste
    EditMenu.add_command(name="cut", command= Cut)
    EditMenu.add_command(name="copy", command= Copy)
    EditMenu.add_command(name="Paste", command= Paste)
    MenuBar.add_cascade(name="Edit", menu= EditMenu)

    # creating help section
    HelpMenu = Menu(MenuBar, tearoff = 0)
        # about notebook
    HelpMenu.add_command(name="about", command= About)
    MenuBar.add_cascade(name="Help", command= HelpMenu)

    root.config(Menu= MenuBar)

    # adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)




root.mainloop()