#creat array using Python List
import numpy as np
#creat a list
list1=[2,3,4,5]
#creat numpy array using list
array1=np.array(list1)
print(array1)
array2=np.zeros(4)
print(array2)
array3=np.ones(7)
print(array3)
# creat an array with values from 0 to 4
array4=np.arange(5)
print("using np.arrangea(5):",array4)
#creat an array with value from 1to8 with a step of 2
array5=np.arange(1,9,2)
print("using np.arange(1,9,2):",array5)
array6=np.random.rand(5)
print(array6)
array7=np.empty(4)
print(array7)
#creat 2D array
#creat 2D array with 2 rows and 4 columns
array8=np.array([[1,2,3,4],
                 [2,3,5,6]])
print(array8)

# creat a 3D array with 2 "slices", each of 3 rows and 4 columns
array9=np.array([[[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]],
                 [[13,14,15,16],
                  [17,18,19,20],
                  [21,22,23,24]]])
print(array9)
# array10=np.array([[[1,2,3,4],[3,4,5,6]],[2,3,4,5]])
# print(array10)
array11=np.full((2,2),5)
print(array11)
array12=np.zeros((2,4,4))
print(array12)
print(array12.ndim)
print(type(array12))
array13=np.ones((1,3,5))
print(array13)
print(array13.ndim)
array14=np.random.rand()
print(array14)

