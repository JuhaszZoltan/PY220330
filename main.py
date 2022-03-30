from module import Pontszerzo, create_helsinki2, get_ermek, get_osszpontszam, get_pontszerzok, get_tobberem

pontszerzok:list[Pontszerzo] = get_pontszerzok('helsinki.txt')

print('3. feladat:')
print(f'Pontszerző helyezések száma: {len(pontszerzok)}')
print('4. feladat:')
get_ermek(pontszerzok)
print('5. feladat:')
print(f'Olimpiai pontok száma: {get_osszpontszam(pontszerzok)}')
print('6. feladat:')
get_tobberem(pontszerzok, 'uszas', 'torna')
create_helsinki2(pontszerzok)