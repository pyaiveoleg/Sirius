from math import sqrt
n = 600851475143 #наименьшее простое, на которое делится данное число - это 19
m=0

def prost(x):
    for i in range(2, int(sqrt(x)) + 1):
        if (x % i == 0):
            return False
    return True

for i in range (19,int (sqrt(n))+1):
    if n%i == 0:
        if prost(i) and (m<i):
            m = i
        if prost(int(n/i)) and (m<i):
            m = i
print (m)