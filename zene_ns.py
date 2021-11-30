def beolvasas():
    zenek = []

    with open("playlist.csv", "r", encoding="utf-8") as file:
        sorok = file.readlines()        #A fájl összes sorának beolvasása 

        for sor in sorok:               #beolvasott sorok bejárása
            sor = sor.strip()           #Eltávolítjuk a sorvége 
            darabok = sor.split(";")    #Feldaraboljuk a sort pontosvesszők mentén

            #A feldarabolás után eltároljuk a zene adatait egy dictionary-ben
            zene = {"eloado": darabok[0], "cím": darabok[1], "mufaj": darabok[2], "hossz": int(darabok[3])}

            zenek.append(zene)

    return zenek

#2.fél

def teljes_hossz(zenek):
    hossz = 0

    for zene in zenek:
        hossz += zene["hossz"]
    
    hossz_perc = hossz // 60
    hossz_masodperc = hossz % 60

    with open("02_hossz.txt", "w", encoding="utf-8") as file:
        file.write(f"A lejátszási lista hossza: {hossz_perc} perc, {hossz_masodperc} masodperc \n")