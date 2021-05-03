a=input()
#print(a)
u=[]
l=[]
e=[]
o=[]
f=[]
for z in a:
    if z.isalpha():
        if (ord(z)>=65) and (ord(z)<=90):
            u.append(z)
        else:
            l.append(z)
    else:
        if(int(z)%2==0):
            e.append(z)
        else:
            o.append(z)
u.sort()
l.sort()
o.sort()
e.sort()
f.extend(l)
f.extend(u)
f.extend(o)
f.extend(e)
print(u)
print(l)
print(o)
print(e)
print(f)
final="".join(f)
print(final)
