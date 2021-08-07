import array as ar
a=ar.array('d')

print(a)
a= ar.array('d',[1.2,1.3,2.3])
print(a)

# Finding the length of an array
a=ar.array('d', [1.1 , 2.1 ,3.1] )
print("length of an array is: ",len(a))


# Accessing array elements in python
a=ar.array( 'd', [1.1 , 2.1 ,3.1] )
print("Second element of an array is: ", a[1])

# Adding the value at the end
a=ar.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print("Append element: ", a)

# Adding more than one elements
a=ar.array('d', [1.1 , 2.1 ,3.1] )
a.extend([4.5,6.3,6.8])
print("Extend element: ",a)

# Insert at particular position
a=ar.array('d', [1.1 , 2.1 ,3.1] )
a.insert(2,3.8)
print("Insert elements: ",a)

# Array concatenation
# Pop/removing elements from the last
a=ar.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print("pop element is: ", a.pop())
print("pop third element is: ",a.pop(3))

#Remove from the start
a=ar.array('d',[1.1 , 2.1 ,3.1])
a.remove(1.1)
print("Remove element is: ",a)

#Slicing an array
a=ar.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
print("Slicing array: ",a[0:3])


