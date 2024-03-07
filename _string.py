age=36
txt="my name is \"priya\" i am {}"  #\"___\" for comma
print(txt.format(age))
print(txt)
print("\f")
age=4
r="i m priya"+" "+str(age) #age="4" than "i m priya+age"
print(r)

quantity=4
itemno=567
price=34.67
myorder="i want {} pieces of item {} for {} dollars"
print((myorder.format(quantity,itemno,price)))
myorder="i want {2} pieces of item {0} for {1} dollars"
print((myorder.format(quantity,itemno,price)))
x=3
y=4
print(x^y) #bit or opretion

t="       my name :is priyA"
print(t.upper())
print(t.lower())
print(len(t))
print(t.strip())#removes any whitespace from the beginning or the end:
print(t.split(":"))
w="i m priya"
print(w.replace("priya","pooja"))


a="""hii  
my name is priya
i m pursuing msc statistics""" # multiple quotes
print(a) # triple quotes
print(a[2])
for x in "banana":
    print(x)
for a in ("priya"):
    print(a)
txt = "Hello\bWorld!" #erases one character (backspace)
print(txt)

b="infividhya is best"
print("infividhya" in b)
print("z" in b)
print("yes"not in b)
if "best" in b:
    print("best, 'in' b")
if "priya" not in b:
    print("priya is not in b")

g = """lorem ipsum DOLOR sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua sed."""
print(g.capitalize()) # first letter upper case
print(g.casefold())
 #print(g.center(1,"m"))
print(g.count("sed"))

# y="i m priya uy"
# print(y.find("uy"))
