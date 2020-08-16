a=input("")
b=input("")
c={}
d={}
f=1
e=1
if len(a)!=len(b):
    print("not")
    
else:
    for i in a:
        if i  not in c:
            c[i]=1
            
        else:
            f=f+1
            c[i]=f
    for i in b:
        if i  not in d:
            d[i]=1
            
        else:
            e=e+1
            d[i]=e
if c==d:
    print("yes")