from tkinter import *
root = Tk()
txt = Text(root, height=15, width=45, font="verdana 20")
txt.pack()
txt.get('1.2')
'd'
txt.get('1.2','1.5')
'dir'
txt.insert('2.3','XXX')
txt.delete('2.3')
txt.delete('2.3','2.5')
txt.insert(END,"\nMaharashtra")
txt.delete('1.0', END)
root.destroy()
