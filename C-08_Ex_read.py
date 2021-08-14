#
# Title: Read data from .xlsx file/ .csv file  in Python
# Date 09 August 2021
# Description: This program that read or exract the data from .xlxs file/ .csv file in Python and reflect the output in command prompt or IDLE 
#
# Copyright: Ruchi Sharma Â© 2021
# 
# @author  Ruchi Sharma
 
# @version 1.0.1	2021-08-09 Reading data from .xlsx file in Python 
# 


#import all the required library
import xlrd
import openpyxl


# location of the .xlsx file
loc= (r"value.xlsx")

#open the workbook
wb= xlrd.open_workbook(loc)
worksheet = wb.sheet_by_index(0)

#read and print the file content
i=0
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True
while(i<10):
	name= worksheet.cell(i,0)
	mrks=worksheet.cell(i,1)
	print(" ",str(name.value), "   ",str(mrks.value))
	i=i+1
 
