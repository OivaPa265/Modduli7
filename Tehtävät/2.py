
def nimet():
    annetut=[]

    while True:
        syote = input("nimi ")

        if syote not in annetut:
            annetut.append(syote)
        elif syote in annetut:
            print("tuon nimi on jo kerran annettu")

        if syote =="":
                break

    print("kaikki nimet")
    for syote in annetut:
         print(syote)
nimet()