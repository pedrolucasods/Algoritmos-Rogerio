chuva = input('está chovendo ?')
dia = input('está de dia ?')

if (chuva == 'não') and (dia == 'sim'):
    print('vamos a praia')
    
elif (chuva == 'sim') or (dia == 'não'):
    print('não vamos a praia!')
