#2-100 prímek
"""
for x in range(101,1,-2):
    print (x)
"""
for szám in range(2,101):
    for osztó in range(2, szám//2+1):#így oldható meg hogy a 4 ne legyen prím
        if(szám % osztó) ==0:
            break 
        else:
            print(szám,'Prím')