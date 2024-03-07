# dict={}
# dict['one']="this is one" #[] define key
# print(dict)
# dict[2]="this is two"
# print(dict)
# dict1={"name":"priya popat","age":22,"city":"porbandar"}
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
dict2={"name":"priya","code":23,"city":"amd","age":[22,56],"job":"student"}
print(dict2)
print(dict2.values())

# adding element into list
# dict2["clg"]="Gu"
# print(dict2)
dict2.update({"clg":"Gu"})
print(dict2)
print(dict2["city"])
print(type(dict2))
gala=dict(name="empire",floor=7,no=727)
print(gala)
print(type(gala))
x=gala.get("name")
print(x)
y=gala.items()
print(y)
if "name" in gala:
    print("yes it is one of the key")
gala["name"]="priya"
print(gala)


