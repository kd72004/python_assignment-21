def number(n):
    if(n>0):
        number(n-1)
        print(n)

number(10)