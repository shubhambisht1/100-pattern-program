#54321
#5432
#543
#54
#5
n=int(input("enter row:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end="")
    print()
