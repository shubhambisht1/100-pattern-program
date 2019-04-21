   #    1
   #   123
   #  12345
   # 1234567
n=int(input("enter row:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()
