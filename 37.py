  #    A
  #   ccc
  #  eeeee
  # ggggggg
n=int(input("enter row:"))
for i in range(1,n+1):
    print(" "*(n-i),(chr(64+(2*i-1))*(2*i-1)))
