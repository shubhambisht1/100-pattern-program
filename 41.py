    #   A
    #  CBA
    # EDCBA
n=int(input("enter row:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(chr(64+j),end="")
    print()
