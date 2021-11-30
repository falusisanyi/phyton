bulizok_szama = int(input("A házinuliban résztvevők száma: "))
rendorok_szama = int(input("A rendőrök száma"))
print()

if rendorok_szama == 0:                     #Ha nincs rendőr akkor mem kapnek el senkit se
    print("minden bulizo menekűlt!")
else:
    elkapottak_szama = 0                    #Változó az elkapott bulizóknak a számának

    for i in range(1, rendorok_szama + 1):  #Minden rendőr elkap valamennyi bulizót
        elkapottak_szama += i               #Az 1. rendőr 1, a 2. rendőr 2, a 3. rendőr 3
    
    if elkapottak_szama < bulizok_szama:    #ha nem kaptak el minden bulizót
        elmenekultek_szama = bulizok_szama - elkapottak_szama
        print(elkapottak_szama, "bulizót elkaptak,", elmenekultek_szama, "menekült el.")
    else:           #ha minden bulizót elkaptak
        print("Ajaj, mindenkit sitre vágtak!")