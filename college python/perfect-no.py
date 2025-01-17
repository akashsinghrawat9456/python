def perfectno(a):
 s=0
 f=0
 for i in range(1, a):
   if a%i==0:
    s=s+i
    f=f+1
 print("factor=",f)
 print("sum of factor=",s)
 if s==a:
   print("it is a perfect number")
 else:
  print("it is not a perfect number")
  



a=int(input("enter the number"));
perfectno(a)



