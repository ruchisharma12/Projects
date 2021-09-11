import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, 'Ruchi')
sheet1.write(2, 0, 'Mohit')
sheet1.write(3, 0, 'Aditya')
sheet1.write(4, 0, 'Viresh')
sheet1.write(5, 0, 'Rajvir')
sheet1.write(0, 1, 'Ashfak')
sheet1.write(0, 2, 'Karan')
sheet1.write(0, 3, 'Anirudh')
sheet1.write(0, 4, 'Manik')
sheet1.write(0, 5, 'Tanmoy')

wb.save('xlwt example.xls')
