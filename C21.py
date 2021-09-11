# Python program to demonstrate writing to CSV

import csv
	
details = ['First_Name', 'Last_Name', 'DOB', 'Place']
	
# data rows of csv file
Students = [ ['Ruchi', 'Sharma', '17-10-2001', 'Sirsa'],
		['Mohit', 'Aggarwal', '20-04-1999', 'Ambala'],
		['Aditya', 'Singh', '14-03-2000', 'Mullana'],
		['Ashfak', 'Us Salehin', '30-06-1998', 'Mullana'],
		['Manik', 'Deshwal', '27-09-1999', 'Rewari'],
		['Rajvir', 'Singh', '12-08-2002', 'Hisar']]
	
# name of csv file
filename = "students_records.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(details)
	csvwriter.writerows(Students)
