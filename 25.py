#  1
# 2 2
#3 3 3
n=int(input("enter row:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
