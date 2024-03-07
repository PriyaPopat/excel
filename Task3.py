# a="*"
# for i in range(1,5):
#     print(a*i)
#
# a=" 1 "
# for i in range(1,5):
#     print(a*i)
#
# rows=4
# number=1
# for i in range(1,rows+1):
#     for j in range(i):
#         print(number,end=" ")
#         number=number+1
#     print("\r")

rows=4

for i in range (1,rows+1):
    print(" "*(rows-i)+" *"
                       ""*i,end=" ")
    print()







