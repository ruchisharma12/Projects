class Student:
	avg=0
	def __init__(self,rollno,name,marks):
		self.rollno=rollno
		self.name=name
		self.marks=marks

	def display(self):
		print(self.name)
		print(self.rollno)
		print(self.marks)
		print(self.avg)

	def average(self):
		self.avg=self.marks/400*100

p1 = Student(190011,"Ruchi",85)
p2 = Student(190012,"Sameer",83)
p3 = Student(190013,"Riya",0)

p1.average()
p2.average()
p3.average()

p1.display()
p2.display()
p3.display()