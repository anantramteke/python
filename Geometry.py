from tkinter import*
root = Tk()
root.title("Volume of sphere")
root.geometry("600x400+500+200")

def sphereVolume():
     r = int(t1.get())
     v =4/3 * 3.14 *(r*r*r)
     l2['fg']='GREEN'
     t2.insert(End,v)

l1 = Label(root, text="Enter the radius:", font="Consolac 15 bold")
t1 = Entry(root, font="Consolac 15")
l2 = Label(root, text="Volume of sphere Displays here..." , font="consolac 15 bold")
t2 = Entry(root, font="Consolac 15")
btn = Button(root, text="Volume", font="Consolac 15 bold", command ="sphereVolume")

l1.pack()
t1.pack()
l2.pack()
t2.pack()
btn.pack()
root.mainloop()
