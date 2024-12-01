# potřebuju nacist input
# rozdelit do dvou sloupcu - např podle mezery (jine moznosti?)
# seradim sloupec 1 a nasledne sloupec 2 vzestupne
# klidne muzu cislo ze sloupce 1 odecist od cisla ze sloupce 2
# vysledek dosadit do sloupce 3
# cislo ktere vyjde nasadit jako absolutni hodnotu - nebudu mit minus
# secti vsechny cisla ve sloupci 3 a vyhod mi to cislo

def prvni():
    file = open("1.input", "r")
    pole1 = []
    pole2 = []
    soucet = 0
    for line in file:
        pole1.append(line.strip().split("   ")[0])
        pole2.append(line.strip().split("   ")[1])
    pole1.sort()
    pole2.sort()
    cislo_radku1 = 0
    for radek in pole1:
        rozdil = abs(int(radek) - int(pole2[cislo_radku1]))
        soucet = soucet + rozdil
        cislo_radku1 = cislo_radku1 + 1
    file.close()
    return soucet


def druhy():
    file = open("1.input", "r")
    pole1 = []
    pole2 = []
    soucet = 0
    for line in file:
        pole1.append(line.strip().split("   ")[0])
        pole2.append(line.strip().split("   ")[1])
    for radek2 in pole1:
        opakovani = pole2.count(radek2)
        soucet = soucet + (int(radek2) * opakovani)
    file.close()
    return soucet


print("Result of first part: {}".format(prvni()))
print("Result of second part: {}".format(druhy()))
