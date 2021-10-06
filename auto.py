"""
név = input('Hogy tisztelhetem fényességedet? ')
print('Üdvözöllek, nagyságos', név, '!', sep='')
szám1 = input('Mely szám a legkedvesebb szívednek? ')
szám1 = int(szam1) #típuskonverzió
szám2 = int(input('S melyik legyen a kedvenced a számok végtelen sokságából? '))
print('Eme két szám szorzata pediglen', szám1*szám2, 'lészen')
"""
"""
#2
nev = input("mi a neved pampogó?")
nap = input("milyen nap van ma?")
print("Üdv ezen a szép', nap,'-n, kedves ', név, sep = ")
"""

#3
autó = input('Egy autónevet kérek! ')
végsebesség = int(input('Egy autó sebességét ide a zaciba! ' + autó + '? '))
ország = input('Hol készült el a ' + autó + '? ')

mondat1 = ország + ' vidékein készül a ' + autó + ', ami ' + str(végsebesség) + ' km/h végsebességre képes ez a beast.'
print(mondat1)

mondat2 = '{} vidékein készül a {}, amo {} km/h végsebességre képes.'.format(orszag, autó, végsebesség)
print(mondat2)

mondat3a = '{0} vidékein készül a {1}, ami {2} km/h végsebességre képes.'.format(ország, autó, végsebesség)
print(mondat3a)

mondat3b = '{2} vidékein készül a {0}, ami {1} km/h végsebességre képes.'.format(ország, végsebesség, autó)
print(mondat3b)

mondat4 = '{o} vidékein készül a {a}, ami {v} km/h végsebességre képes.'.format(o=ország, a=autó, v=végsebesség)
print(mondat4)

mondat5 = '{} vidékein készül a {a}, ami {} km/h végsebességre képes.'.format(ország, végsebesség, a=autó)
print(mondat5)

mondat6 =f'{ország} vidékein készül a {autó}, ami {végsebesség} km/h végsebességre képes.'
print(mondat6)