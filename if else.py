#a=10
#b=45
#print(a+b)
#if(a>b):
 #   print("a is max")
#else:
 #   print("b is max ")
#c=23
#if a>b:
 #   print("a is max")
#elif b>c:
   # print("b is max")
#else:
   # print("c is max")
a=12
b=2
c=7
if a>b and a>c:
    print("a is max")
elif b>c and b>a:
    print("b is max")
else:
    print("c is max")

# number is prime or not
i=2
a=int(input("enter number:"))
if (i<a and a%i==0):
    print("a is not prime")
else:
    print("a is prime")