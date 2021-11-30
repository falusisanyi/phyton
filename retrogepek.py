tipus = input('Milyen típusú gépe van?')
ár = input('Mennyi az ára?')
állapot = input ('ELindul és működik e a gépe?')

if tipus == 'ZX Spectrum':
    print('Megfelelő')
elif tipus != 'ZX Spectrum':
    print('Nem megfelelő')
if ár <= '25000Ft':
    print('Megfelelő árú')
elif ár >= ('25000Ft'):
    print('Nem megfelelő')
if állapot == 'igen':
    print('Nagyszerű')
elif állapot != 'nem':
    print('Nem megfelelő')

print (f'{tipus} megfelelő {ár} megfelelő {állapot}megfelelő.')

