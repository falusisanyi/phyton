név = input('Mi a gép neve? ')
működik = True if input('Működik i/n ') == 'i' else False
ár = int(input('Mi az ára? '))

if (név =='ZX Spectrum' or név == 'C64') and működik and ár <= 25000:
    print('Binnisz!')
else:
    print('Gagyi fos No Binnisz.')

