def rev_num(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n//=10
    print(r)

rev_num(123)