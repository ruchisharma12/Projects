#
# Title: Example of Radio button, Checkbox, Combobox and Listbox  in Python
# Date 11 August 2021
# Description: This shows various example of Radio button, Checkbox, Combobox and Listbox in Python and reflect the output in command prompt or IDLE 
#
# Copyright: Ruchi Sharma Â© 2021
# 
# @author  Ruchi Sharma
 
# @version 1.0.1	2021-08-11    Radio button, Checkbox, Combobox and Listbox 
# 

#import all the required library
import tkinter as tk
from tkinter import *  
from tkinter import ttk

#fix the GUI window title and size
top = Tk() 
top.title(" Widgets: RadioButton, CheckBox, ComboBox, ListBox")
top.geometry("600x600")


def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)


var = IntVar()
CheckVar1= IntVar()



head = tk.Label(top, text="Goggle Form", background='blue', foreground="white",font = ("Times New Roman", 15)).grid(row = 0, column = 1,padx = 200, pady = 15) 
name = Label(top, text = "Name").place(x = 50,y = 50)


# label for name 
label = Label(top, text = "Designation :", font = ("Times New Roman", 10)).place(x=50,y=80)


# Adding combobox drop down list 
# Combobox creation 
n1 = tk.StringVar() 
posOpt = ttk.Combobox(top, width = 17, textvariable = n1) 
# Adding combobox drop down list 
posOpt['values'] = (' Faculty','Student', 'Others') 
posOpt.place(x=170,y=80)
posOpt.current()




#label for rollno and password and set their position
roll = Label(top, text = "Roll No:").place(x = 50, y = 120) 
e1 = Entry(top).place(x = 170, y = 50) 

password = Label(top, text = "Password").place(x = 50, y = 150)
e2 = Entry(top).place(x = 170, y = 120)


# create listbox object 
# Define a label for the list.   
label = ttk.Label(top, text = " Courses").place(x=50, y=180)  

listbox = Listbox(top, selectmode=SINGLE, height = 5, width = 20, bg = "white", activestyle = 'dotbox', font = ("Times New Roman", 10), fg = "black") 

# insert elements by their 
# index and names.
listbox.insert(1, "Engineering") 
listbox.insert(2, "LAW") 
listbox.insert(3, "Medical") 
listbox.insert(4, "Pharmacy") 
listbox.insert(5, "Agriculture") 

# pack the widgets 
#label 
listbox.place(x=170, y=180) 

e3 = Entry(top).place(x = 170, y = 150)
 


  
# pack the widgets 

listbox.place(x=170, y=180) 

#set Label
n2 = tk.StringVar()
country = ttk.Label(top, text = " Country").place(x=50,y=300)
countryOpt = ttk.Combobox(top, width = 17, textvariable = n2) 
# Adding combobox drop down list 
countryOpt['values'] = (' India',' China',' Australia',' Malaysia',' Italy',' Turkey',' Canada')
 
countryOpt.place(x=110,y=300)
countryOpt.current()


#set label
n3 = tk.StringVar()
state = ttk.Label(top, text = " State").place(x=245,y=300)
stateOpt = ttk.Combobox(top, width = 17, textvariable = n3) 

# Adding combobox drop down list 
stateOpt['values'] = (' Haryana',' Punjab',' Rajasthan',' Maharashtra',' Uttar Pardesh') 
stateOpt.place(x=290,y=300)
stateOpt.current()

n4 = tk.StringVar()
city = ttk.Label(top, text = " City").place(x=420,y=300)
cityOpt = ttk.Combobox(top, width = 17, textvariable = n4) 

# Adding combobox drop down list 
cityOpt['values'] = (' Sirsa', ' Hisar', ' Rewari', ' Noida', ' Sonipat') 

cityOpt.place(x=460,y=300)
cityOpt.current()



# label
label = Label(top, text = "Phone No", font = ("Times New Roman", 10)).place(x=50,y=340)
e4 = Entry(top).place(x = 170, y = 340) 


gender= Label(top, text="Gender",font = ("Times New Roman", 10)).place(x=50,y=370)

R1= Radiobutton(top, text="Male", variable= var, value =1).place(x=170, y=370)
R2= Radiobutton(top, text="Female", variable= var, value =1).place(x=240, y=370)

# The Check Buttons
C1 = Checkbutton(top, text = "Fill all the entries", variable = CheckVar1, onvalue = 1, offvalue = 0, width = 20).place(x= 50, y =400)


showButton = Button(top, text = "Submit",bd="6", bg="blue", fg="white").place(x = 50, y = 450)
quitbtn = Button(top, text="QUIT",  fg="red", bd= 4, command = quit).place(x=190, y=450)
top.mainloop()