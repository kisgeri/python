'''
osztály = [['Noémi', 'l', 15, 'noemi@hipp.hopp'],
           ['Dezső', 'f', 17, 'dezso2@nyikk.nyekk'],
           ['Gizella', 'l', 16, 'gizi@pikk.pakk'],
           ['Edömér', 'f', 16, 'edo@itt.ott']]
for tag in osztály:
    print(tag[0], ": ", tag[-1], sep='')
    
összeg = 0
for tag in osztály:
    összeg += tag[2]
 
print('Az osztály átlagéletkora', összeg/len(osztály), 'év.')

lányok = 0 
for tag in osztály: 
    if tag[1] == 'l':
        lányok += 1
 
if lányok > len(osztály) - lányok:
    print('A lányok vannak többen.')
elif lányok < len(osztály) - lányok:
    print('A fiúk vannak többen.')
else:
    print('A fiúk pont annyian vannak, mint a lányok.')
    
for tag in osztály:
    print(tag[0])
nev = input("írj be a fenti nevekből egyet ")
for tag in osztály:
    for index in range(len(tag)):
        if tag[index] == nev:
            print(tag[-1])
            break

def szótáraz(magyar_szó):
    szótár = [['nagy', 'big'], ['pici', 'tiny'],
              ['én', 'I'], ['foci', 'soccer'],
              ['ott', 'there'], ['szarvas', 'deer'],
              ['soha', 'never']]
    for szó in szótár:
        if szó[0] == magyar_szó:
            return szó[1]
        elif szó[1] == magyar_szó:
            return szó[0]
    return 'Nincs ilyen szó a szótárban.'
kérdezett_szó = None
while kérdezett_szó != '':
    kérdezett_szó = input('Melyik magyar szóra vagy kíváncsi? ')
    if kérdezett_szó != '':
        print(kérdezett_szó, 'keresésének eredménye:',szótáraz(kérdezett_szó))
'''
szótár = {'nagy': 'big', 'pici': 'tiny',
          'én': 'I', 'foci': 'soccer',
          'ott': 'there', 'szarvas': 'deer',
          'soha': 'never'}
'''
kérdezett_szó = None
while kérdezett_szó != '':
    kérdezett_szó = input('Melyik magyar szóra vagy kíváncsi? ')
    if kérdezett_szó != '':
        print(kérdezett_szó, 'keresésének eredménye:',szótár.get(kérdezett_szó, 'Nincs ilyen szó.'))

osztály = [{'név': 'Noémi', 'nem': 'l', 'kor': 15},
           {'név': 'Dezső', 'nem': 'f', 'kor': 17},
           {'név': 'Gizella', 'nem': 'l', 'kor': 16},
           {'név': 'Edömér', 'nem': 'f', 'kor': 16}]
for tag in osztály:
    if tag['név'] == 'Dezső':
        print(tag['kor'])
        osztály = {'Noémi': {'nem': 'l', 'kor': 15},
                   'Dezső': {'nem': 'f', 'kor': 17},
                   'Gizella': {'nem': 'l', 'kor': 16},
                   'Edömér': {'nem': 'f', 'kor': 16}}
print(osztály['Dezső']['kor'])

összeg = 0
for tag in osztály:
    összeg += osztály[tag]['kor']
print('Az osztály átlagéletkora', összeg/len(osztály), 'év.')

lányok = 0 
for tag in osztály: 
    if osztály[tag]['nem'] == 'l':
        lányok += 1
'''
ív = {'egyik hegedűs': [1, 1, 1, 1, 1],
      'másik hegedűs': [1, 1, 1, 1, 0],
      'brácsás': [1, 1, 0, 0, 0],
      'csellós': [0, 1, 1, 1, 1]}
vonosok_jelenletei = []
for vonos in ív.values():
    vonos_jelen = sum(vonos)
    vonosok_jelenletei.append(vonos_jelen)

sorszam = vonosok_jelenletei.index(min(vonosok_jelenletei))

print("A(z)", list(ív.keys())[sorszam], "hiányzott a legtöbbet jelen")

for nap_indexe in range(5):
    mind_jelen_voltak = True
    for vonos, jelenlet in ív.items():
        if jelenlet[nap_indexe] == 0:
            mind_jelen_voltak = False
            break
    if mind_jelen_voltak:
        print(f"A(z) {nap_indexe+1}. napon minden vonós jelen volt.")
        
bevételek = [[130,156,231,112,96,311,231],
             [29,15,210,11,191,14,302],
             [143,222,98,101,184,201,87],
             [133,132,182,121,148,199,187]]
legnagyobb_különbség = 0
legnagyobb_különbség_helye = None
for index in range(len(bevételek)):
    különbség = max(bevételek[index]) - min(bevételek[index])
    if különbség > legnagyobb_különbség:
        legnagyobb_különbség = különbség
        legnagyobb_különbség_helye = index
print('A legnagyobb különbség:', legnagyobb_különbség, 'ami ebben a boltban volt:', legnagyobb_különbség_helye+1)

boltok_ösz = []

első = sum(bevételek[0])
második = sum(bevételek[1])
harmadik = sum(bevételek[2])
negyedik = sum(bevételek[3])
boltok_ösz.append(első)
boltok_ösz.append(második)
boltok_ösz.append(harmadik)
boltok_ösz.append(negyedik)
print(boltok_ösz)

for index in range(len(boltok_ösz)):
    sorszam = boltok_ösz.index(max(boltok_ösz))
print('A(z) ', sorszam+1, '. boltnak volt a legnagyobb a bevétele', sep='')
