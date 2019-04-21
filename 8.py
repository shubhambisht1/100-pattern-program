#dddd
#cccc
#bbbb
#aaaa
n=int(input("enter the row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-i),end="")
    print()
