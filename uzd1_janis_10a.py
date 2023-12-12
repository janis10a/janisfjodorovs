gads = int(input('ievadiet gadu: '))#ievāc datus no programmas izmantotāja
if gads%4 == int(): #dala ar 4, jo ja dalās ar 4, tad tas ir garais, vai īsais gads.
    print(gads,'ir garais gads.')
elif gads%4 != int():#atkal dala ar 4 lai pārbaudītu, vai tas ir garais, vai īsais gads.
    print(gads,'ir īsais gads.')
