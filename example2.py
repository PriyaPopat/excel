# delet any variable
counter=78
print(counter)
del counter
print(counter)

# check the type of variable
# a="priya"
# b=22
# c=12.11
# print(type(a))
# print(type(b))
# print(type(c))

# casting python variables
a = str(10)
b = int(10)
c = float(10)
print(a,b,c)

print(type(a))
print(type(b))
print(type(c))

# check case sensitivity
age=22
Age=45
print(age)
print(Age)

# in single line we can assign multiple variables
p=q=r=23
print(p,q,r)

a,b,c=12,56,34
print(a,b,c)

a,b,c=10,45,"priya"
print(a,b,c)
# task
# leap year or not
# check a program is even or odd
# program to identify wheather a given alphabate is vowel or not
# age classifier less than 12 child 20-29 adult
# prime number or not

w=True
y=1+4j
z=False
print(type(w))
print(type(y))
print(type(z))

str="hello world!"
print(str)
print(str[0])
print(str[3:7])
print(str[:])
print(str[:11])
print(str*2)
print(str+"hi")

# a=[10,"priya",45.89,True,2j+1]
# print(a)
# print(a[0:4])

list=[10,"priya",45.89,True,2j+1]
print(list)
print(list[3:7])
list1=[23]
print(list+list1)
print(list*2)
print(type(list))
list[0:4]=4,4,"rt"
print(list)