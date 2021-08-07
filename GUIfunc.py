import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog as fd
import collections
from collections import Counter
import math
 
top = Tk()  
top.geometry("600x500")
top.title("GUI APP - Correlation in Python")

myText=StringVar()
list1 = [1,2,5,7,9,6,7,3,4]
n= len(list1)
list1.sort()

def browse():
	name=fd.askopenfilename()
	messagebox.showinfo("File Selected:", name)


def mean():
	mean= (sum(list1)/n)
	myText.set("Mean is: %f"%(mean))

def mode():
	count = collections.Counter(list1)
	max_value = max(list(count.values()))
	mode = [number for number, freq in count.items() if freq == max_value] 			
	myText.set("Mode is: %s"%str(mode))

def median():
	if((n%2)==0):
    		median =list1[(n/2)]+list1[(n/2)+1]/2
	else:
    		median = list1[int(n/2)+1]
	myText.set("Median is: %f"%(median))


def std():
	std = 0
	add = 0
	mean= (sum(list1)/n)
	for i in list1:
		sq= (i-mean)**2
		add = add+ sq
	
	p= add/n
	std = math.sqrt(p)
	myText.set("Standard deviation is: %.5f"%(std))


x = Label(top, text = "Select the data file .xls/.xlsx", font=("Arial", 20)).place(x = 150,y = 10)
 
         

browseBt = Button(top, text = "Browse File", command=browse, font=("Arial", 10)).place(x=400, y=70)
inputtxt = tk.Text(top,height = 2,width = 20).place(x = 200,y = 50)
#inputtxt.pack()

res = Label(top, text = "", textvar=myText, fg="blue", font=("Arial",12)).place(x = 200,y = 150)
myText.set("The result will be shown here")

button1 = Button(top, text = "Mean" , font=("Arial", 10), command= mean).place(x = 100, y = 200,width=150)
button2 = Button(top, text = "Mode" , font=("Arial", 10), command= mode).place(x = 300, y = 200,width=150)
button3 = Button(top, text = "Median" , font=("Arial", 10),command= median).place(x = 100, y = 250,width=150)
button4 = Button(top, text = "Standard Deviation" , font=("Arial", 10), command= std).place(x = 300, y = 250,width=150)

result = Entry(top).place(x = 100, y = 600,width=300,height=100) 


quit = Button(top,text="QUIT", fg="red",command=quit , font=("Arial", 10)).place(x=250, y=300)

top.mainloop()