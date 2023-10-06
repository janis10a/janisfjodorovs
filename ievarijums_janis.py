aboli = int(input('cik kg ābolu jums ir? '))
cukurs = 1
udens = 0.5
citrons = 1
ekstrakts = 5
kanelis = 10
ccukurs = 1.35
cudens=0
ccitrons=0.58
cekstrakts = 17
ckanelis = 0.60
if aboli >= 0:
    serves = round(aboli / 3)
    print('jums āboli pietiek ievārijuma servēm: ', serves )
    print('jūsu ievārijumam vajadzēs: ','cukurs(kg):',cukurs*serves, '   ūdens (litri)', udens*serves, '     citroni (gb)', citrons*serves, '     ekstrakts (ml)', ekstrakts*serves, '     kanēlis(g)', kanelis*serves)
    print('jūsu izmaksas sastāvdaļām(eiro):  ', 'cukurs:',round(ccukurs*serves),'     citroni',round(ccitrons*serves),'      ekstrakts:17','   kanelis:',round( ckanelis*serves))


