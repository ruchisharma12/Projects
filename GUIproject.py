import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog as fd
 
top = Tk()  
top.geometry("600x500")
top.title("GUI APP - Correlation in Python")

def browse():
	name=fd.askopenfilename()
	messagebox.showinfo("File Selected:", name)

x = Label(top, text = "Select the data file .xls/.xlsx", font=("Arial", 20)).place(x = 150,y = 10)
          

browseBt = Button(top, text = "Browse File", command=browse, font=("Arial",10)).place(x=400, y=70)
inputtxt = tk.Text(top,height = 2,width = 20).place(x = 200,y = 50)
#inputtxt.pack()

res = Label(top, text = "Result of the data will be shown here", fg="blue", font=("Arial",12)).place(x = 200,y = 150)
#res.pack_forget()
button1 = Button(top, text = "Mean" , font=("Arial", 10)).place(x = 100, y = 200,width=150)
button2 = Button(top, text = "Mode" , font=("Arial",10)).place(x = 300, y = 200,width=150)
button3 = Button(top, text = "Median" , font=("Arial", 10)).place(x = 100, y = 250,width=150)
button4 = Button(top, text = "Standard Deviation" , font=("Arial", 10)).place(x = 300, y = 250,width=150)

result = Entry(top).place(x = 100, y = 600,width=300,height=100) 


quit = Button(top,text="QUIT", fg="red",command=quit , font=("Arial", 10)).place(x=250, y=300)

top.mainloop()