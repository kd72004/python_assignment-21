def odd_number(n):
    if(n>0):
        odd_number(n-1)
        if(n%2!=0):
            print(n)
odd_number(10)