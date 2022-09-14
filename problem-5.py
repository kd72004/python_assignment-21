def even_num(n):
    if(n>0):
        even_num(n-1)
        if(n%2==0):
            print(n)

even_num(10)