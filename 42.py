  #    0
  #   101
  #  21012
  # 321012
n=int(input("enter row:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(i-j,end="")
    for k in range(i):
        print(k,end="")
    print()
