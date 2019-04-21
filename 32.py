#EEEEE
# DDDD
#  CCC
#   BB
#    A
n=int(input("enter row:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(chr(64+n+1-i),end="")
    print()
