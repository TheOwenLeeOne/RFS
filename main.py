from tkinter import Tk, Label, Button, Entry
from tkinter.filedialog import askdirectory
import os
import random

class MainGui:

    directory = ""
    files = []


    def __init__(self, master):
        self.master = master
        self.master.title("Random File Selector")
        self.master.minsize(500,400)

        self.label = Label(master, text="Enter a directory:")
        self.label.grid(row=0)

        self.file_textbox = Entry(master)
        self.file_textbox.grid(row=0, column=1)


        self.close_button = Button(master, text="Close", command=master.quit)


        self.directory_button = Button(master, text="...", command=self.selectDirectory)
        self.directory_button.grid(row=0,column=3)

        self.file_button = Button(master, text="Select File", command=self.fileButtonClick)
        self.file_button.grid(row=1)    

        self.filenameLabel = Label(master, text="File will go here")
        self.filenameLabel.grid(row=2)
            
    def fileButtonClick(self):
        self.selectFile(self.directory, self.files)

    def selectDirectory(self):
        self.directory = askdirectory() + "/"
        print(self.directory)
        self.filenameLabel.configure(text=self.directory)
        self.files = os.listdir(self.directory)

    def selectFile(self, directory, fileList):
        file = fileList[random.randint(0, len(fileList)-1 )]
        if("." in file):
            print(directory + file)
            os.startfile(directory + file)
        else:
            newDir = directory + file + "/"
            self.selectFile(newDir,os.listdir(newDir))

root = Tk()
my_gui = MainGui(root)
root.mainloop()