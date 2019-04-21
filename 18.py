#aaaaa
#bbbb
#ccc
#dd
#e
n=int(input("enter row:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+i),end="")
    print()
