# *-- coding: utf-8 --*
# PyEdit 1.0
# Copyright Anirudh Balaji
# DO NOT ERASE!!!!!
# Nobody shall replicate, modify or electronically or physically transmit this script in any way without this copyright.
# from idlelib.MultiCall import r

from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
filename = 'Untitled'
ifile = open('interpreter', 'r')
interpreter = ifile.read()

def new():
    global filename
    filename = 'Untitled'
    textw.delete(0.0, END)

def save():
    global filename
    if filename == 'Untitled':
        saveas()
    else:
        text = textw.get(0.0, END)
        f = open(filename, 'w')
        f.write(text)
        f.close()

def saveas():
    global filename
    filename = asksaveasfilename()
    f = open(filename, 'w')
    t = textw.get(0.0, END)
    f.write(t)
    f.close()

def openf():
    global filename
    filename = askopenfilename()
    f = open(filename, 'r')
    textw.delete(0.0, END)
    t = f.read()
    textw.insert(0.0, t)

def seti():
    i = Tk()
    i.title('Interpreter')
    iq = Button(i,text='Quit', command = i.quit)
    iq.pack()
    def iset():
        global interpreter
        i = askopenfilename()
        ifile = open('interpreter', 'r+')
        ifile.write(i)
        interpreter = ifile.read()
        ifile.close()
    ib = Button(i,text='Set Interpreter...', command = iset)
    ib.pack()
    i.mainloop()


def about():
    a = Tk(root)
    a.title('About')
    l = Label(a,text='About PyEdit 1.0')
    li = Label(a,text='PyEdit is made for and built on Python.\nIt is very good but is missing key features.\nBye bye!\nMade by Anirudh Balaji')
    q = Button(a,text='Quit', command = a.quit)
    l.pack()
    li.pack()
    q.pack()
    a.mainloop()
    
def run():
    global interpreter
    global filename
    import os
    os.system(interpreter + ' ' + filename)
    
    

root = Tk()
root.title('PyEdit')
root.geometry('400x400')

textw = Text(root)
textw.pack()
menu = Menu(root)
fileMenu = Menu(menu)
fileMenu.add_command(label='New', command = new)
fileMenu.add_command(label='Open', command = openf)
fileMenu.add_command(label='Save', command = save)
fileMenu.add_command(label='Save As', command = saveas)
fileMenu.add_separator()
fileMenu.add_command(label='Quit', command = root.quit)
runmenu = Menu(menu)
runmenu.add_command(label='Interpreter', command = seti)
runmenu.add_command(label='About', command = about)
runmenu.add_separator()
runmenu.add_command(label='Run', command = run)
menu.add_cascade(label='File', menu=fileMenu)
menu.add_cascade(label='Run', menu=runmenu)

root.config(menu=menu)
root.mainloop()




