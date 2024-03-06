f = open("lorem.txt", "r")
linijka = f.readline()
while linijka:
    print(linijka)
    linijka = f.readline()
f.close()
#program czyta wszytskie linijki z tekstu
