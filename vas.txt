OLVADÁSI_PONT = 1539
FORRÁSSI_PONT = 2750

hőfok = int(input('Hőfok: '))

if hőfok < OLVADÁSI_PONT:
    print('Szilárd')
elif hőfok > FORRÁSSI_PONT:
    print('folyékony')
else:
    print('Gáz')
    
