def square_rev(n):
    if(n>0):
        
        square_rev(n-1)
        print(n*n*n)

square_rev(10)