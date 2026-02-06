# tekee tyhjän listan johon nimet lisätään
def nimet():
    annetut=[]
# kysyy käyttäjältä nimiä kunnes tämä syöttää tyhjän
    while True:
        syote = input("nimi ")
    # tarkistaa jos annetu nimi ei ole jo annettu
        if syote not in annetut:
            annetut.append(syote)
            #Jos annetu nimi on jo kerran annetu printtaa tämän
        elif syote in annetut:
            print("tuon nimi on jo kerran annettu")
    # jos syote on tyhjä lopettaa ohjelman
        if syote =="":
                break
# printtaa sanan kaikki nimet
    print("kaikki nimet")
    # printtaa kaikki annetut nimet kerran siinä järjestyksessä jossa ne ovat annettu
    for syote in annetut:
         print(syote)
# kutsuu nimi listaa
nimet()
