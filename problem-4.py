def odd_rev(n):
    if(n>0):
        if(n%2!=0):
            print(n)
        odd_rev(n-1)
        

odd_rev(10)