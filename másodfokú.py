import math 

a= float(input('Kérem a másodfokú egyenlet főegyütthatóját'))
while a==0:
    print('Ez nem lesz megoldható')
    a= float(input('Kérem a másodfokú egyenlet főegyütthatóját'))
    

b= float(input('Kérem az elsőfokú tag együtthatóját'))
c= float(input('Kérem a konstans tagot'))
d= b*b-4*a*c
print(d)

if d>=0:
    x1= (-b+math.sqrt(d))/(2*a)
    x2= (-b-math.sqrt(d))/(2*a)
    print(x1)
    print(x2)
    print('Van valós megoldás')

else:
    print('Nincs valós megoldás')
    x1= (-b)+(math.sqrt(d))/(2*a)
    x2= (-b)-(math.sqrt(d))/(2*a)
    print(x1)
    print(x2)
    print('Nincs valós megoldás')

    