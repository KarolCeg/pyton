f = open("lorem.txt", "r")
linijka = f.readline()
while linijka:
    print(linijka)
    linijka = f.readline()
f.close()
#program czyta wszytskie linijki z tekstu


----------------------- liczenie ile razy co wystąpiło
def literki(nazwa):
    s =dict()
    for znak in nazwa:
        s[znak] = 0
    for znak in nazwa:
        if(znak in s.keys()):
            s[znak] +=1
    return s
linijka = "ala ma kota"
print(literki(linijka))

---------------- z pliku zczytanie i liczenie
def literki(nazwa):
    s = dict()
    linijka = nazwa.readline()
    while linijka:
        for znak in linijka:
            if znak in s:
                s[znak] += 1
            else:
                s[znak] = 1
        linijka = nazwa.readline()
    return s

f = open("tekst.txt", "r")
print(literki(f))
f.close()












