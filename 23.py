#edcba
#edcba
#edc
#ed
#e
n=int(input("enter row:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+n+1-j),end="")
    print()
