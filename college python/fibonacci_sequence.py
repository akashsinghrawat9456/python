a=int(input("enter the range"))
def fibo(a):
    
       b=0
       c=1
       print(b)
       print(c)
       for i in range (2,a):
        d=b+c
        b=c
        c=d
        print(c)
fibo(a)