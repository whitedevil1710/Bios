a=list(map(int,input("Enter the number:").split()))
b=0
for i in a:
    if i>0:
        n=i
        temp=n
        r=0
        while n>0:
            d=n%10
            r=r*10+d
            n=n//10
        if temp==r:
            b=1
    else:
        b=0
        break
if b==1:
    print("True")
else:
    print("False")
    
