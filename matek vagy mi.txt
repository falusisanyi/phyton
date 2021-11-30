egyik = int(input("Adjon meg egy számot"))
masik = int(input("Adkon meg egy másik számot"))
jel = input("Adkon meg egy műveleti jelet")

#print('A művelet eredménye: ',end='' )

if jel == '+':
    print(egyik+masik)
elif jel == '-':
    print(egyik-masik)
elif jel == '%':
    print(egyik % masik)
elif jel == '/':
    print(egyik / masik)
elif jel == '>>':
    print(egyik ''>>'' masik)
