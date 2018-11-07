a = []
a.append(1)
a.append(2)
i=1
s = 2
while a[i]<4e6:
    a.append(a[i]+a[i-1])
    if (a[i+1]<4e6) and (a[i]%2==0):
        s+=a[i+1]
    i+=1
print (s)