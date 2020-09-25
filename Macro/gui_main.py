import tkinter as tk
from tkinter import Tk, Label, Button, Listbox, simpledialog
import backend_main as bm
from os import listdir

class Main_GUI:
    def __init__(self, master):
        self.master = master

        master.geometry("230x240")
        master.title("Macro-Recorder")

        self.label = Label(master, text="Esc to stop recording")
        self.label.pack()
        
        self.startButton = Button(master, text="Start", command=self.start)
        self.startButton.pack()

        self.saveButton = Button(master, text="Save", command=self.save)
        self.saveButton.pack()

        self.playButton = Button(master, text="Play", command=self.play)
        self.playButton.pack()
        
        self.label = Label(master, text="Saves: ")
        self.label.pack()

        self.listbox = Listbox(master)
        self.listbox.bind('<Double-1>', self.currentSave)
        self.listbox.pack()
        
        self.updateSaveslist()


    def start(self):
        bm._main("record")
        return

    def play(self):
        cs = self.listbox.curselection()
        saves = listdir(bm.savesFp)
        if int in cs:
            bm.Play(bm.savesFp  + saves[cs[0]])
        else:
            bm.Play(bm.dataFp)

    def save(self):
        fileName = simpledialog.askstring("Input", "Enter File Name: ")
        bm.Save(fileName)
        self.updateSaveslist() 
        return

    def updateSaveslist(self):
        self.listbox.delete(0, tk.END)
        saves = listdir(bm.savesFp)
        for i in range(len(saves)):
            self.listbox.insert(i, saves[i])

    def currentSave(self, event):
        cs = self.listbox.curselection()
        return(cs)

root = Tk()
my_gui = Main_GUI(root)
root.mainloop()
