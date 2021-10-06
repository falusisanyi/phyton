év = int(input('Kérem adja meg az évet amiben van'))
if (év%4!=4):
    print('Ez nem szökű év')
elif (év%400==0):
    print('Szükő ív')
elif (év%100==0):
    print('Ez az ív sem szökik ma el.')
else:
    print('Na ez már szökő év mo')


    


    