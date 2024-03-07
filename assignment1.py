# Create a 1D NumPy array with elements from 1 to 10.
import numpy as np
oneD_array=np.arange(1,11)
print(oneD_array)
print(type(oneD_array))
print(oneD_array.ndim)

# Create a 2D NumPy array with a shape of (3, 4) containing random integers.

twoD_array=np.random.rand(3,4)
print(twoD_array)
print(twoD_array.ndim)

# Perform element-wise addition, subtraction, multiplication, and division on two arrays.

# Extract and print the elements at even indices from a 1D array

even_1Darray=np.arange(2,13,2)
print(even_1Darray)
print(even_1Darray.ndim)

# #Create a 2-D array
# 1 3 5
# 7 9 2
# 4 6 8
#  access the second row of the array
#  access the third column of the array

twoDarray=np.array([[1,3,5],[7,9,2],[4,6,8]])
print(twoDarray)
print(twoDarray.ndim)
print(twoDarray[1])
print(twoDarray[0:3,2:])

# Create a 3D array with shape (2, 3, 4) and access a specific element of the array [1,2,1]

threeD_array=np.random.rand(2,3,4)
print(threeD_array)
print(threeD_array.ndim)
print(threeD_array[1,2,1])

#Save one of your created arrays to a text file

np.savetxt("newtextfile.txt",twoDarray)

# Load the saved array back into a NumPy array.
l=np.loadtxt("newtextfile.txt")
print(l)

maths=np.array([56,89,33])
a=(maths[0])
print(a)
ss=np.array([89,5,6])
b=(ss[0])
print(b)
eng=np.array([3,4,5])
c=(eng[0])
print(c)
#per=(sum(maths)/300)*100
# print(per)
per=np.add(maths[0]+ss[0]+eng[0])
print(per)