#eeeee
#dddd
#ccc
#bb
#a
n=int(input("enter row:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+n+1-i),end="")
    print()
