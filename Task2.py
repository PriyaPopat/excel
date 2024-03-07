# task
# leap year or not
# check a program is even or odd
# program to identify wheather a given alphabet is vowels or not
# age classifier less than 12 child 20-29 adult
# prime number or not

# leap year or not

year=int(input("enter number:"))

if year%4==0:
    print("leap year")
else:
    print("not leap year")

# even or odd

number=int(input("enter number"))
if number%2==0:
    print("number is even")
else:
    print("number is odd")

# alphabet is vowels or consonants

alphabet=(input("enter alphabet:"))

if alphabet=="a"or"e"or"i"or"o"or"u":
    print("alphabet is vowel")
else:
    print("hi")

    # age classification
age=int(input("enter age:"))
if age<=12:
    print("child")
elif age <= 19:
    print("teenage")
elif age <= 29:
  print("adult")
elif age <=45:
    print("y")
else:
    print("senior")


