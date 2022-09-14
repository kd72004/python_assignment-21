def square(n):
    if(n>0):
        square(n-1)
        print(n*n)

square(10)