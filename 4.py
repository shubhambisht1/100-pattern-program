#AAAAA
#BBBBB
#CCCCC
#DDDDD
n=int(input("enter the row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end="")
    print()
