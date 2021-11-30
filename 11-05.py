nev = input("Kérem adja meg a nevét: ")
eletkor = int(input("Kérem adja meg az életkorát: "))

if eletkor <= 3:
    rang=("Totyogóknak a kettes számrendszerről")
elif eletkor <= 6:
    rang=("Hackeljük meg az óvodát!")
elif eletkor <=14:
    rang=("Felhőtechnológia a menzán")
elif eletkor <=18:
    rang=("Big data a középiskolában")
if eletkor >= 18:
    int(input("Kérem adja meg az életkorát: "))

print(f'{nev} aki {eletkor} éves, akinek ez jár {rang}')