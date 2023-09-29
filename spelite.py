import random
#spele akmens skeres papirs
gajieni = ['akmens','papirs','skeres']#saraksts
while True: 
    cilveka_gajiens = input('ievadi gājienu:')
    datora_gajiens =random.choice(gajieni)
    print('Cilvēks:', cilveka_gajiens,'vs dators', datora_gajiens)
    if cilveka_gajiens == datora_gajiens:print('neizšķirts')
    elif cilveka_gajiens == 'akmens' and datora_gajiens == 'skeres': print('cilvēks uzvar!')
    elif cilveka_gajiens == 'papirs' and datora_gajiens == 'akmens': print('cilvēks uzvar!')
    elif cilveka_gajiens == 'skeres' and datora_gajiens == 'papirs': print('cilvēks uzvar!')
    elif cilveka_gajiens == 'akmens' and datora_gajiens == 'papirs': print('dators uzvar!')
    elif cilveka_gajiens == 'skeres' and datora_gajiens == 'akmens': print('dators uzvar!')
    elif cilveka_gajiens == 'papirs' and datora_gajiens == 'akmens': print('dators uzvar!')
    else: print('dators uzvar!')