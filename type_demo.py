import numpy as np
# int_array=np.array([1,2,3,4])
# print(int_array)
# print(int_array.dtype)
# float_array=np.array([1.2,2.3,1,12])
# print(float_array.dtype)
# complex_array=np.array([1+2j,2+3j])
# print(complex_array.dtype)
# string_array=np.array(["pya678","t"])
# print(string_array.dtype)
#
# a={"name":"piya","surname":"popat","age":12}
# v=np.array(a)
# print(v.dtype)

array1=np.array([[[4.56,6,8.9,6,0],[4,5,6,9,7]]])
print(array1.ndim)
print(array1.astype('int32'))
print(array1.shape)
print(array1.size)
print(array1.dtype)
print(array1.itemsize)
print(array1.data)
array=np.array([[1,2,3],[23,4,3]])
np.save('array.npy',array)
a=np.load('array.npy')
print(a)
np.savetxt('array.txt',array)
w=np.loadtxt('array.txt')
print(w)
print(w.dtype)
array23=np.array([[1,2,3,4,5],[2,3,4,4,5]])
print(array23)
array23[-1,-5],array23[-2,-4]=34,45
print(array23)
# array23[0,0],array23[1,1]=89,4
# print(array23)
# print(array23[1,1])
# array14=np.array([1,2,3,4,5])
#
# array14[3]=5
# print(array14)
# print(array)
# array14[-5]=23
# print(array14)

array15=np.array([[[1,2,3],[2,3,4]],[[11,12,13],[14,15,16]]])
print(array15.ndim)
print(array15[1,1,0])