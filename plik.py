f = open("lorem.txt", "r")
linijka = f.readline()
while linijka:
    print(linijka)
    linijka = f.readline()
f.close()
#program czyta wszytskie linijki z tekstu


-----------------------
def literki(nazwa):
    s = dict()
    for znak in nazwa:
        if (znak in s.keys()):
            s[znak] +=1
    return s

f = open("tekst.txt", "r")
linijka = f.readline()
linijka
print(literki(linijka))
"""while linijka:
    print(linijka)
    linijka = f.readline()"""
f.close()


def literki1(nazwa):
    f = open("nazwa.txt", "r")
    linijka = f.readline()
    f.close
