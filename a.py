from tkinter import *

# initallization
window = Tk()

label = Label(text="Please enter your name\n",bg="black",fg="white")
ent = Entry()
btn = Button(text="Ok?")

# end init

def onclick():
    global ent
    global label
    txt = ent.get()
    label.config(text=txt)
    ent.delete(0,len(txt))

btn.config(command=onclick)

label.pack()
ent.pack()
btn.pack()

window.mainloop()