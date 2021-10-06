import math 

a= input('Kérem a másodfokú egyenlet főegyütthatóját')
a= float(a)
while a==0:
    print('Ez nem lesz megoldható')
    a= input('Kérem a másodfokú egyenlet főegyütthatóját')
    a= float(a)

b= float(input('Kérem az elsőfokú tag együtthatóját'))
c= float(input('Kérem a konstans tagot'))
d= b*b-4*a*c
print(d)

if d>=0:
    x1= (-b+math.sqrt(d)/2*a)
    x2= (-b-math.sqrt(d))/(2*a)
    print('Az egyik megoldás', x1)
    print('A másik megoldás', x2)
else:
    print('Nincs valós megoldás')
    x1= (-b-math.sqrt(d))/(2*a)
    x2= (-b+math.sqrt(d))/(2*a)
    print('Az egyik megoldás', x1)
    print('A másik megoldás', x2)