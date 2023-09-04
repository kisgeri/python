
het52=[]
for _ in range(5):
    lottoszamok_52 = input("mi legyen az 52. hét lotto számai?(egyesével adja meg) ")
    het52.append(lottoszamok_52)
def length(num):
    return len(str(num))

def value(num):
    return num
sorted_numbers = sorted(het52, key=lambda num: (length(num), value(num)))
print(sorted_numbers)

with open("./fajl/lottoszamok.csv","r") as fajl:
    szamok=[]
    for sor in fajl:
        adatok = sor.strip()
        szamok.append(adatok)
    print(szamok)
    het=int(input("mondj egy hetett 1-51 között: "))
    for index in range(len(szamok)):
        if index+1 == het:
            print(szamok[index])
    print(szamok[het - 1])
    nem_huztak = []
    for i in range(1, 100):
        huztak = False
        for het in szamok:
            if str(i) in het.split():
                huztak = True
                break
        if not huztak:
            nem_huztak.append(i)

    if nem_huztak:
        print("Az alábbi számokat nem húzták ki az 51 héten:", nem_huztak)
    else:
        print("Minden szám legalább egyszer ki lett húzva az 51 héten.")
    szam = []
    for het in szamok:
        szam.append(het.split())
    paratlan=0
    for sor in szam:
        for darab in sor:
            if darab[-1] == "1":
                paratlan+=1
            elif darab[-1] == "3":
                paratlan+=1
            elif darab[-1] == "5":
                paratlan+=1
            elif darab[-1] == "7":
                paratlan+=1
            elif darab[-1] == "9":
                paratlan+=1
    print(paratlan)

minden = []
for het in szamok:
    minden.append(het)
for het in het52:
    minden.append(het)
for het in sorted_numbers:
    minden.append(het)

with open("./fajl/lotto52.txt","w") as cfajl:
    for hetszamok in minden:
        sor = " ".join(hetszamok) + "\n"
        cfajl.write(sor)
