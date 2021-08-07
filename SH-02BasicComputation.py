import math
from collections import Counter

print("Enter the ten values: ")

# Declaring an array of length 5
num =[5,4,5,3,1]
num.sort()
n= len(num)


# compute mean
sum = 0
mean = 0
for x in num:
	sum = sum+x
mean= sum/n	
print("mean is: ",mean)


# compute median
med= 0
if n%2==0:
	med= num[n/2]
else: 
	x= num[n//2]
	y=num[n//2 -1]
	med= int((x+y)/2)

print("Median is: ", med)

# compute mode
data = Counter(num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print("Mode is: ",get_mode)



# compute standard deviation
std = 0
add = 0
for i in num:
	sq= (i-mean)**2
	add = add+ sq
	
p= add/n
std = math.sqrt(p)
print("Standard deviation is: ", std)

