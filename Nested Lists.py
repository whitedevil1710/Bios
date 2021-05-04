s=int(input())
l=[]
d=[]
for i in range (s):
    n=input()
    f=float(input())
    l.append([n,f])
    d.append(f)
d=sorted((d))
m=d[1]
n=[]
for j in l:
    if m==j[1]:
        n.append(j[0])
n.sort()
for nm in n:
    print(nm)
