diak = ['Kiss', 'Péter', '10.A', 17, True, False]

print(diak[3])

diak = {
	'vezetéknév': 'Kiss',
	'keresztnév': 'Péter',
	'osztály': '10.A',
	'Életkor': 17,
	'kollágista': True,
	'info_fakt': False, 
	'matek_jegyek': [5, 4, 4, 3, 5, 5]
}
print(diak['Életkor'])

raktar = {
114589: 'Dominyó póc',
264875: 'íróasztal',
364879: 'Kényelmes fotel',
568974: 'evőasztal 6 fős'
}

print (raktar)

diakok = [['Kiss', 'Péter', '10.A', 17, True, False], ... ]

diak = {
	'vezetéknév': 'Kiss',
	'keresztnév': 'Péter',
	'osztály': '10.A',
	'menza': True
}

print(diak.get('szakkor', 'nincs adat'))
print(szakkor in diak)

diak['szakkor'] = True
print(diak)

diak['Életkor'] = 17
print(diak)

del diak['vezetéknév']
print(diak)
for kulcs in diak:
	print(kulcs, diak[kulcs])

print(diak.value())
for ertek in diak.values():
	print(ertek)

for kulcs, ertek in diak.items():
	print(kulcs, ertek)