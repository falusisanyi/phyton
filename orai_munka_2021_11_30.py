import random

szam1 = int(input("Kérek egy számot gae: "))
szam2 = random.randrange(10 , 50)
szam3 = 5
#halmaz
szamok2 = {}
szamok2.add(5)
szamok2.add(6)
szamok2.add(7)
#lista
szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(szam3)
if szam1 %2 == 0:
    print("páros")
else:
    print("páratlan")