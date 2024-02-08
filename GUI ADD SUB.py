<<<<<<< HEAD
from tkinter import * 
root = Tk()
root.title("First GUI Program")
root.geometry('400x400+400+160')

def addition():
    txtResult.delete(0,END)
    x = int(txtNum1.get())
    y = int(txtNum2.get())
    ans = x+y
    txtResult.insert(END,ans)   #txtResult.insert(0,ans)
    return

def subtraction():
    txtResult.delete(0,END)
    x = int(txtNum1.get())
    y = int(txtNum2.get())
    ans = x-y
    txtResult.insert(END,ans)   #txtResult.insert(0,ans)
    return

def clearData():
    txtNum1.delete(0,END)
    txtNum2.delete(0,END)
    txtResult.delete(0,END)
    txtNum1.focus()
    return

lblNo1 = Label(root,text="First No.:", font="verdana 14")
lblNo2 = Label(root,text="Second No.:", font="verdana 14")
lblResult = Label(root,text="RESULT", font="verdana 14")

txtNum1 = Entry(root,font="verdana 14")
txtNum2= Entry(root,font="verdana 14")
txtResult = Entry(root,font="verdana 14")


bntAdd = Button(root, text="ADD", font="verdana 14",command=addition)
bntExit = Button(root, text="EXIT", font="verdana 14", command=root.destroy)
bntSub = Button(root, text="SUB", font="verdana 14", command=subtraction)
bntClear = Button(root, text="CLEAR", font="verdana 14", command=clearData)


lblNo1.grid(row=0,column=0, padx=10, pady=10)
txtNum1.grid(row=0,column=1, padx=10, pady=10)

lblNo2.grid(row=1,column=0, padx=10, pady=10)
txtNum2.grid(row=1,column=1, padx=10, pady=10)

lblResult.grid(row=2,column=0, padx=10, pady=10)
txtResult.grid(row=2,column=1, padx=10, pady=10)

bntAdd.grid(row=3, padx=10, pady=10)
bntExit.grid(row=3,column=1, padx=10, pady=10)

bntSub.grid(row=4,column=0, padx=10, pady=10)
bntClear.grid(row=4,column=1, padx=10, pady=10)

root.mainloop()
=======
from tkinter import * 
root = Tk()
root.title("First GUI Program")
root.geometry('400x400+400+160')

def addition():
    txtResult.delete(0,END)
    x = int(txtNum1.get())
    y = int(txtNum2.get())
    ans = x+y
    txtResult.insert(END,ans)   #txtResult.insert(0,ans)
    return

def subtraction():
    txtResult.delete(0,END)
    x = int(txtNum1.get())
    y = int(txtNum2.get())
    ans = x-y
    txtResult.insert(END,ans)   #txtResult.insert(0,ans)
    return

def clearData():
    txtNum1.delete(0,END)
    txtNum2.delete(0,END)
    txtResult.delete(0,END)
    txtNum1.focus()
    return

lblNo1 = Label(root,text="First No.:", font="verdana 14")
lblNo2 = Label(root,text="Second No.:", font="verdana 14")
lblResult = Label(root,text="RESULT", font="verdana 14")

txtNum1 = Entry(root,font="verdana 14")
txtNum2= Entry(root,font="verdana 14")
txtResult = Entry(root,font="verdana 14")


bntAdd = Button(root, text="ADD", font="verdana 14",command=addition)
bntExit = Button(root, text="EXIT", font="verdana 14", command=root.destroy)
bntSub = Button(root, text="SUB", font="verdana 14", command=subtraction)
bntClear = Button(root, text="CLEAR", font="verdana 14", command=clearData)


lblNo1.grid(row=0,column=0, padx=10, pady=10)
txtNum1.grid(row=0,column=1, padx=10, pady=10)

lblNo2.grid(row=1,column=0, padx=10, pady=10)
txtNum2.grid(row=1,column=1, padx=10, pady=10)

lblResult.grid(row=2,column=0, padx=10, pady=10)
txtResult.grid(row=2,column=1, padx=10, pady=10)

bntAdd.grid(row=3, padx=10, pady=10)
bntExit.grid(row=3,column=1, padx=10, pady=10)

bntSub.grid(row=4,column=0, padx=10, pady=10)
bntClear.grid(row=4,column=1, padx=10, pady=10)

root.mainloop()
>>>>>>> 102239ee99a83bb6fd0a0bcdf6dc1ebe220126b2
