   #   A
   #  ABC
   # ABCDE
n=int(input("enter row:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(chr(64+j),end="")
    print()
