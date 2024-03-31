from tkinter import *

# def click():

def submit():
    input = text.get("1.0",END)
    input(input)
 
windows = Tk()

windows.geometry("450x450")

text = Text(windows, bg="light yellow", font=("segos Print",60), height=4, width=10, padx=20,pady=20,fg="blue")
text.pack()
button = Button(windows,command=submit,text='click me')
button.pack()

windows.mainloop()