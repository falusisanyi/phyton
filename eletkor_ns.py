#1 feladat
szam = input('Kérem adjon meg egy negatív egész számot')
kor = input('Kérem adja meg az életkorát')

if kor < 13:
    minősítés = 'gyermek'
if kor < 17:
    minősítés = 'Fiatalkorú'
if kor < 23:
    minősítés = 'ifjú'
if kor < 59:
    minősítés = 'felnőtt'