from tkinter import * 
root = Tk()
root.title("First GUI Program")
root.geometry('400x400+400+160')

def show():
    print("Current Status = ", status.get())

status = IntVar()

#chkCri = Checkbutton(root, text="Cricket", font="verdana 14", variable=status, command = show, onvalue=99, offvalue=9999)

chkCri = Checkbutton(root, text="Cricket", font="verdana 14", variable=status, command = show, indicatoron=0)

#status.set(1)
chkCri.pack()


root.mainloop()
