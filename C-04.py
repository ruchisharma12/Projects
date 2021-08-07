from tkinter import *  
top = Tk()  
top.geometry("800x800")



name = Label(top, text = "Name").place(x = 30,y = 50)

email = Label(top, text = "Email").place(x = 30, y = 90)  
password = Label(top, text = "Password").place(x = 30, y = 130)

e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 95, y = 130)

login_btn = PhotoImage(file='click.jpg')

button1= Button(top, image=login_btn).place(x=10,y=220)


showButton = Button(top, text = "Display",bd="10", bg="blue", fg="white").place(x = 30, y = 170)
quitbtn = Button(top, text="QUIT",  fg="red", bd= 4, command = quit).place(x=190, y=170)
top.mainloop()