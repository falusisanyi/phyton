import random
egyik = random.randint(1,10)
másik = random.randint(1.10)
összeg = egyik+másik
print('Összeg')
if(egyik % 2 == 2):
    print('Páros')
    if összeg % 3 == 0:
        print('Osztható hárommal')
    else:
        print('Nem osztható hárommal')
    

    
    
