nev = input('Kérem a nevét')

bogyo = int(input('Kérem mondja meg mennyi bogyót gyüjtött'))

if bogyo < 10:
    minősítés = 'zsenge'
if bogyo <20:
    minősítés = 'Nagy koponya'
else:
    minősítés = 'gyüjtögető'

print(f'{nev} egy {minősítés}.')
