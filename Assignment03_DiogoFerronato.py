import math

points = int(input("Enter the number of polygon points: "))
n = points
n1 = 0
x = []
y = []

while n1 < n:
    x.append(float(input(f"Type the X coordinate of the point {n1+1}: ")))
    y.append(float(input(f"Type the Y coordinate of the point {n1+1}: ")))
    n1 = n1 + 1

print(f"\nPoint        {'x':<15} {'y':<10}")
print("-"*33)
for n in range(n):
    print(f"{n+1} {x[n]:15.2f} {y[n]:15.2f}")

Ax = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0
xt = 0
yt = 0
Ixt = 0
Iyt = 0
Ixyt = 0

print(f"\nGeometric characteristics:")

x.append(x[0])
y.append(y[0])
n = points

for i in range(n):
    Ax = (((x[i+1]+x[i])*(y[i+1]-y[i]))/2 + Ax)
    Sx = -((x[i+1]-x[i])*(y[i+1]**2+y[i]*y[i+1]+y[i]**2))/6 +Sx
    Sy = ((y[i+1]-y[i])*(x[i+1]**2+x[i]*x[i+1]+x[i]**2))/6 +Sy
    Ix = -((x[i+1]-x[i])*(y[i+1]**3+y[i+1]**2*y[i+1]+y[i+1]*y[i]**2+y[i]**3))/12 + Ix
    Iy = ((y[i+1]-y[i])*(x[i+1]**3+x[i+1]**2*x[i+1]+x[i+1]*x[i]**2+x[i]**3))/12 + Iy
    Ixy = -((y[i+1]-y[i])*(y[i+1]*(3*x[i+1]**2+2*x[i+1]*x[i]+x[i]**2)+y[i]*(3*x[i]**2+2*x[i+1]*x[i]+x[i+1]**2)))/24 + Ixy

Ax=abs(Ax)
Xt = Sy/Ax
Yt = Sx/Ax
Ixt = Ix - Yt**2*Ax
Iyt = Iy - Xt**2*Ax
Ixyt = Ixy + Xt*Yt*Ax

print(f"Ax:{Ax:>10.2f}")
print(f"Sx:{Sx:>10.2f}")
print(f"Sy:{Sy:>10.2f}")
print(f"Ix:{Ix:>10.2f}")
print(f"Iy:{Iy:>10.2f}")
print(f"Ixy:{Ixy:>9.2f}")
print(f"Xt:{Xt:>10.2f}")
print(f"Yt:{Yt:>10.2f}")
print(f"Ixt:{Ixt:>9.2f}")
print(f"Iyt:{Iyt:>9.2f}")
print(f"Ixyt:{Ixyt:>8.2f}")
