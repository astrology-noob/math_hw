import math

def func(x):
    return math.sin(x)

def find_root(left, mid, right):
    while abs(func(mid)) > accuracy:
        if func(left)*func(mid) <= 0:
            right = mid
            mid = (left+mid)/2
        else:
            left = mid
            mid = (mid+right)/2
    return round(mid, 4)

left = float(input("левая граница ")) 
right = float(input("правая граница "))
mid = None
accuracy = 0.0001

if func(left) * func(right) <= 0:
    mid = (left+right)/2
    print(find_root(left, mid, right))
else:
    print("нет корня на этом промежутке или он не один")