    #    1
    #   222
    #  33333
    # 4444444
    #
n=int(input("enter no row:"))
for i in range(1,n+1):
    print(" "*(n-i),(str(i))*(2*i-1))
