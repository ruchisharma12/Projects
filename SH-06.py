#
# Title: Conversion of the input string into upper, lower, toggle, sentence and title case
# Date 10 August 2021
# Description: This program takes an input as string and converts it into upper, lower, toggle, sentence and title case and reflects the output in GUI
#
# Copyright: Ruchi Sharma Â© 2021
# 
# @author  Ruchi Sharma
 
# @version 1.0.1	2021-08-10 Converts string into upper, lower, toggle, sentence and title case
# 

#import all the required library
import tkinter as tk
from tkinter import * 
from tkinter import messagebox


#fix the GUI window title and size
top = Tk()  
top.geometry("600x500")
top.title("GUI APP - Correlation in Python")

# this variable are dynamic 
input = StringVar()         #this variable stores and prints the converted string
output= StringVar()         #this variable accepts and pass the string to be converted
\
#this routine converts the string into upper case
def upr():
	ch=output.get()
	input.set(ch.upper())

#this routine converts the string into lower case
def lowr():
	ch=output.get()
	input.set(ch.lower())

##this routine converts the string into toggle case
def togg():
	ch=output.get()
	str=""
	j=0
	for i in ch:
		if(i.isupper()):
			str+= i.lower()
		elif(i.islower()):
			str+=i.upper()
		elif(i.isspace()):
			j=0
			str+=" "
		else:
			str+=""
	input.set(str)

#this routine converts the string into sentence case 
def sent():
	ch= output.get()
	str=""
	j=0
	for i in ch:
		j=j+1
		if(j==1):
			str+= i.upper()
		else:
			str+=i.lower()
		
	input.set(str)

#this routine converts the string into title case
def ttl():
	ch= output.get()
	str=""
	j=0
	for i in ch:
		j=j+1
		if(j==1):
			str+= i.upper()
		elif(i.isspace()):
			j=0
			str+=" "
		else:
			str+=i.lower()
	input.set(str)



 
#this is a label         
x = Label(top, text = "Enter a word or sentence", font=("Arial", 11)).place(x = 45,y = 50)



#this is the place to give input
inputtxt = Entry(top,textvariable =output, font=("Arial", 15))
inputtxt.place(x = 220,y = 50)
inputtxt.focus_set()


#this place is to print the result
res = Label(top, text = "", fg="green",textvariable=input, font=("Arial",12)).place(x = 150,y = 150)
#this is a default message
input.set("Result of the data will be shown here")

#these are the buttons that calls the respective functions
upperBT = Button(top, text = "Upper" , font=("Arial", 10), command=upr).place(x = 100, y = 200,width=150)
lowerBT = Button(top, text = "Lower" , font=("Arial",10), command=lowr).place(x = 300, y = 200,width=150)
titleBT = Button(top, text = "Title" , font=("Arial",10), command=ttl).place(x = 200, y = 250,width=150)
toggle = Button(top, text = "Toggle" , font=("Arial", 10), command=togg).place(x = 100, y = 300,width=150)
sentenceBT = Button(top, text = "Sentence" , font=("Arial", 10), command=sent).place(x = 300, y = 300,width=150)


#this closes the GUI
quit = Button(top,text="QUIT", fg="red",command=quit , font=("Arial", 10)).place(x=250, y=400)

top.mainloop()