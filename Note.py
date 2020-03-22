# Making NotePad app using python
# Functionality include open existing file and save file functionality for now
#Graphical User Interface is done with Tkinter

#Bugs   need to add a scroll bar for overflow element 

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfilename

win = Tk()
win.title("NotePad App")

# functionlity to open an existing file...
def open_file():
    blank.delete("1.0", END)
    file = askopenfile(mode="r", filetypes = [ ("text files", "*.txt") ])
    if file is not None :
        text = file.read()
        blank.insert("1.0", text)


#functionality to save current file
# has bugs when u click cancel when trying to save a file.. 
def save_file():
    notepad_text = blank.get("1.0", "end-1c")
    file = asksaveasfilename(title = "Save", filetypes = [ ("text files", "*.txt") ])
    with open(file, "w") as data :
        data.write(notepad_text)


#Creating the UI 
menubar = Menu(win)
win.config(menu = menubar)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "file", menu = filemenu)
filemenu.add_command(label = "open", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_command(label = "Exit", command = win.destroy)

blank = Text(win, font = ( "Roboto", 14 )) #font should be roboto and font size should be 14 
blank.pack()

win.mainloop()