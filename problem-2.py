def number_r(n):
    if(n>0):
        print(n)
        number_r(n-1)

number_r(10)