#
# Title: Read data from .xlsx file/ .csv file and show in tree view in Python
# Date 13 August 2021
# Description: This program that read or exract the data from .xlxs file/ .csv file in Python and reflect the output in command prompt or IDLE 
#
# Copyright: Ruchi Sharma Â© 2021
# 
# @author  Ruchi Sharma
 
# @version 1.0.1	2021-08-13 Reading data from .xlsx file and showing in tree view in Python 
# 

#import all the required library
import tkinter as tk
from tkinter import ttk
import xlrd
import openpyxl
from tkinter.messagebox import showinfo

#fix the GUI window title and size
root = tk.Tk()
root.title('Treeview')
root.geometry('400x300')

# location of the .xlsx file
loc= (r"value.xlsx")

#open the workbook
wb= xlrd.open_workbook(loc)
worksheet = wb.sheet_by_index(0)

#read and print the file content
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True
i=1
dataValues=[]
while(i<10):
	name=worksheet.cell(i,0)	
	mrks=worksheet.cell(i,1)
	print(" ",str(name.value), "   ",str(mrks.value))
	dataValues.append((str(name.value), str(mrks.value)))
	i=i+1

# columns
columns = ('#1', '#2', '#3')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('#1', text=' Name')
tree.heading('#2', text='Marks')


# adding data to the treeview
for d in dataValues:
    tree.insert('', tk.END, values=d)


# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        #
        showinfo(title='Information',
                message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()