# *-- coding: utf-8 --*
# PyEdit 1.1
# Copyright Anirudh Balaji
# DO NOT ERASE!!!!!
# Nobody shall replicate, modify or electronically or physically transmit this script in any way without this copyright.

from Tkinter import *
# from pyttk import *
from tkFileDialog import *
# from tkMessageBox import showinfo
filename = 'Untitled'

if sys.platform == "win32":
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
    def iqu():
        i.quit()
        root.mainloop()
    iq = Button(i,text='Quit', command = iqu)
    iq.pack()
    def iset():
        global interpreter
        i = askopenfilename()
        ifile = open('interpreter', 'r+')
        ifile.write(i)
        interpreter = ifile.read()
        ifile.close()
    def icls():
        ifile = open("interpreter", "w")
        ifile.write('')
        ifile.close()
    ib = Button(i,text='Set Interpreter...', command = iset)
    il = Button(i, text="Clear Interpreter", command = icls)
    ib.pack()
    il.pack()
    i.mainloop()


def about():
    about = Toplevel(root,background="black")
    about.title('PyEdit | About')

    new_about_desc = '''
About PyEdit 1.3

PyEdit is written for & built on Python. It started when I had my old
computer, thought it would be a fun project. Now, I learnt more about
GUIs so I decided to make this an application. It is good at editing,
executing, etc., but it doesn't have syntax hightlighting. I attempted
it once, but it didn't work. Written by Anirudh Balaji.

Changelog
0.9
Initial release!
1.0
Fixed execution mechanism.
1.1
Added output window to show output.
1.2
Made output window use the Text widget instead of the Label widget.
Added a scrollbar to the output window (p.s. it's bad ☹))
1.3
Removed the scrollbar!!! :)
Added a dark theme.

'''
 

    about_label  = Label(about, text='About PyEdit 1.3', foreground="white", background="black", justify=CENTER)
    change_label = Label(about, text="Changelog", foreground="white", background="black", justify=CENTER)

    description = '''
PyEdit is written for & built on Python. 
It started when I had my old computer, thought it would be a fun project.
Now, I learnt more about GUIs so I decided to make this an application.
It is good at editing, executing, etc., but it doesn't have syntax hightlighting.
I attempted it once, but it didn't work.
Written by Anirudh Balaji
    '''
    changelog = '''
0.9
Initial release!
1.0
Fixed execution mechanism.
1.1
Added output window to show output.
1.2
Made output window use the Text widget instead of the Label widget.
Added a scrollbar to the output window (p.s. it's bad ☹))
1.3
Removed the scrollbar!!! :)
Added a dark theme.
    '''
    about_text = Label(about, text=description, foreground="white", background="black", justify=LEFT)
    change_text = Label(about, text=changelog, foreground="white", background="black", justify=LEFT)

    # about_label.pack()
    # about_text.pack()
    # change_label.pack()
    # change_text.pack()
    new_about_text = Text(about) 
    new_about_text.insert(0.0, new_about_desc)
    new_about_text.config(state="disabled")
    new_about_text.pack()
    about.mainloop()
    
def run():
    global interpreter
    global filename
    import os
    import sys
    if filename == "Untitled":
        saveas()
    if sys.platform == "win32":
        result = os.popen("%s %s" % (interpreter, filename)).read()
        output = Toplevel(root)
        text = Text(output, foreground="white", background="black")
        text.insert(0.0, result)
        text.config(state="disabled")
        text.pack(expand=True, fill=BOTH)
        scroll.pack()
        output.mainloop()
    else:
        result = os.popen("/usr/bin/python %s" % filename).read()
        output = Toplevel(root)
        text = Text(output, foreground="white", background="black")
        text.insert(0.0, result)
        text.config(state="disabled")
        text.pack(expand=True, fill=BOTH)
        output.mainloop()
    
    

root = Tk()
root.title('PyEdit')
root.geometry('400x400')

textw = Text(root, background="black", foreground="white", insertbackground="white")
textw.pack(fill=BOTH, expand=1)
textw.tag_configure("red", foreground="gray")
textw.tag_configure("green", foreground="green")
textw.tag_configure("purple", foreground="#9400D3")
textw.tag_configure("yellow", foreground="#EEEE00")
textw.tag_configure("black", foreground="#000000")
textw.tag_configure("white", foreground="white")

# textw = Text(root)
# textw.pack()
menu = Menu(root, foreground="white", background="black")
fileMenu = Menu(menu, foreground="white", background="black")
fileMenu.add_command(label='New', command = new)
fileMenu.add_command(label='Open', command = openf)
fileMenu.add_command(label='Save', command = save)
fileMenu.add_command(label='Save As', command = saveas)
fileMenu.add_separator()
fileMenu.add_command(label='Quit', command = root.quit)
runmenu = Menu(menu, foreground="white", background="black")
runmenu.add_command(label='Interpreter', command = seti)
runmenu.add_command(label='About', command = about)
runmenu.add_separator()
runmenu.add_command(label='Run', command = run)
menu.add_cascade(label='File', menu=fileMenu)
menu.add_cascade(label='Run', menu=runmenu)

root.config(menu=menu)
root.mainloop()
