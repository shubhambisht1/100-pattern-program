#11111
#222
#33
#44
n=int(input("enter row:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(i,end="")
    print()
