a = []
b = []
m = 0
for i in range (100,999):
    for j in range (100,999):
        k = i*j;
        a = list (map(int,str(k)))
        b = list(reversed(a))
        if (a == b) and (m < k):
            m = k
print (m)