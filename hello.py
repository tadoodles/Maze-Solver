from tkinter import *

root = Tk()

def myClick():
    myLabel3 = Label(root, text="I clicked a Button!")
    myLabel3.pack()


# creating a label widget
myLabel1 = Label(root, text="Hellow Orld!")
myLabel2 = Label(root, text="My name is Aneemo Na Pentose")
myButton = Button(root, text="Click me!", command=myClick)

# shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=3, column=2)


    
root.mainloop()