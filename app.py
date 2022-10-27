import base64
from cgitb import text
from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import string
import hashlib
import os, ntpath, sys
from threading import Thread
from turtle import bgcolor, color
import base64
from attr import s

class App:

    def __init__(self, master, parametre):
        self.master = master
        self.config_windows(master)
        self.isFile = False
        
        frame=ttk.Frame(master, padding='0 5 0 0') 
        frame.grid(row=0, column=0, sticky=N+S+E+W)
        
        Grid.columnconfigure(frame, 1, weight=1) 
        Grid.rowconfigure(frame, 3, weight=1)
        
        self.create_menu(master)
        self.add_controlli(master, frame, parametre)
        self.create_statusBar(frame)
    
    def config_windows(self,master):
        
        master.geometry('{}x{}'.format(700, 128))
        master.minsize(700, 128)
        master.maxsize(1000, 128)
        Grid.rowconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 0, weight=1)
        master = ttk.Label(background="red",relief=FLAT,)
    
    def create_menu(self, master):
        
        menu = Menu(master)
        master.config(menu=menu)
        
        helpmenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.About)
        helpmenu.add_command(label="Origine", command=self.Origine)
        helpmenu.add_command(label="Discord", command=self.Discord)
        helpmenu.configure(bg='red')
    

    def add_controlli(self, master, frame, parametre):
        mylist=['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', "md5"]
        self.var = StringVar(master)
        self.var.set("md5")

        ttk.Label(frame, text="Chaine de caractere").grid(row=0, sticky=W, padx=5, pady=5)
        ttk.Label(frame, text="Type de hash").grid(row=1, sticky=W, padx=5, pady=5)
        ttk.Button(frame, text="Encrypter", command=self.calcola_stringa).grid(row=1, sticky=W, padx=5, pady=5)
        ttk.Label(frame, text="Resultat encrypter").grid(row=2, sticky=W, padx=5, pady=5)
        
        self.e1 = ttk.Entry(frame)
        self.e2 = ttk.Entry(frame)
        self.omenu = ttk.OptionMenu(frame, self.var, *mylist)

        self.e1.grid(row=0, column=1, padx=5, pady=5, sticky=W+E)
        self.omenu.grid(row=1, column=1, padx=5, pady=5, sticky=W+E)
        self.e2.grid(row=2, column=1, padx=5, pady=5, sticky=W+E)
        
        if parametre is not None:
            self.e1.delete(0, END)
            self.e1.insert(0, parametre)
    
    def create_statusBar(self,frame):
        self.status_bar = ttk.Label(frame,background="#80D0D0",relief=FLAT,text="> $ Yazuko and Lirox's")
        self.status_bar.grid(row=3, columnspan=3, sticky=S+W+E)
    
        
    def calcola_stringa(self):
        str = self.e1.get()
        if str == "":
            messagebox.showinfo("Attention", "Veuillez définir une chaine de caractère à encrypter")
            messagebox.showinfo("Report", "En cas de probleme merci de contacter $$$#7296 et Yazuko")
            return
            
        m = self.get_type_of_hash()
        m.update(str.encode('utf-8'))
        self.e2.delete(0, END)
        self.e2.insert(0, m.hexdigest())

    def get_type_of_hash(self):
        if self.var.get() == 'sha1':
            m = hashlib.sha1()
        elif self.var.get() == 'sha224':
            m = hashlib.sha224()
        elif self.var.get() == 'sha256':
            m = hashlib.sha256()
        elif self.var.get() == 'sha384':
            m = hashlib.sha384()
        elif self.var.get() == 'sha512':
            m = hashlib.sha512()
        else:
            m = hashlib.md5()
        return m     
        
    def About(self):
        messagebox.showinfo("Info", "Pour toute question(s) ou autre(s) merci de nous contacter sur Discord : $$$#7296 ou 0xYazuko#9521") 
        messagebox.showinfo("Project", "Project made by Lirox's and Yazuko 2022®")

    def  Discord(self):
        messagebox.showinfo("Discord", "$$$#7296 and 0xYazuko #9521")
    
    def Origine(self): 
        messagebox.showinfo("Origine", "L'origine de £ncrypt viens tout simplement d'une idee de Yazuko et Lirox's ce projet est à la base fait pour vous simplifier la vie.(Encrypter)")

     


def main(argv):
    if len(sys.argv) > 1:
        parametre = sys.argv[1] 
    else:
        parametre = None

    root = Tk()
    root.wm_title("£ncrypt 2022®")
    app = App(root,parametre)
    root.iconbitmap('icona.ico')
    root.wm_title = ttk.Label(root, background="red",relief=FLAT,)
    root.mainloop()
    
if __name__ == '__main__':
    main(sys.argv)
