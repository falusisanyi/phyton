#3 feladat
ELÉGTELEN = 0-29
ELÉGSÉGES = 30-37
KÖZEPES = 38-43
JÓ = 44-49
JELES = 50-55

pontszám = int(input('Kérem adja meg a pontszámot'))

if pontszám <=29:
    print('elégtelen')
if pontszám <=37:
    print('elégséges')
if pontszám <=43:
    print('közepes')
if pontszám <=49:
    print('jó')
if pontszám <=55:
    print('jeles')

