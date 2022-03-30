class Pontszerzo:
    def __init__(self, sor:str):
        darabok:list[str] = sor.strip().split(' ')
        self.helyezes:int = int(darabok[0])
        self.sportolok_szama:int = int(darabok[1])
        self.sportag:str = darabok[2]
        self.versenyszam:str = darabok[3]
        self.pontszam:int = 7 if self.helyezes == 1 else 7 - self.helyezes


def get_pontszerzok(f:str) -> list[Pontszerzo]:
    pontszerzok:list[Pontszerzo] = []
    for s in open(f):
        pontszerzok.append(Pontszerzo(s))
    return pontszerzok


def get_ermek(lst:list[Pontszerzo]) -> None:
    arany:int = 0
    ezust:int = 0
    bronz:int = 0
    for p in lst:
        if p.helyezes == 1: arany += 1
        elif p.helyezes == 2: ezust += 1
        elif p.helyezes == 3: bronz += 1
    print(f'Arany: {arany}')
    print(f'Ezüst: {ezust}')
    print(f'Bronz: {bronz}')
    print(f'Összesen: {arany + ezust + bronz}')


def get_osszpontszam(lst:list[Pontszerzo]) -> int:
    op = 0
    for p in lst:
        op += p.pontszam
    return op


def get_tobberem(lst:list[Pontszerzo], sn1:str, sn2:str) -> None:
    sn1_ermek = 0
    sn2_ermek = 0
    for p in lst:
        if p.helyezes in [1, 2, 3]:
            if p.sportag == sn1: sn1_ermek += 1
            elif p.sportag == sn2: sn2_ermek += 1
    if sn1_ermek > sn2_ermek:
        print(f'{sn1.capitalize()} sportágban szereztek több érmét')
    elif sn1_ermek < sn2_ermek:
        print(f'{sn2.capitalize()} sportágban szereztek több érmét')
    else:
        print(f'{sn1.capitalize()} és {sn2} sportágakban egyenlő volt az érmek száma')


def create_helsinki2(lst:list[Pontszerzo]) -> None:
    f = open("helsinki2.txt", 'w')
    for p in lst:
        sn:str = 'kajak-kenu' if p.sportag == 'kajakkenu' else p.sportag
        f.write(f'{p.helyezes} {p.sportolok_szama} {p.pontszam} {sn} {p.versenyszam}\n')
    f.close()