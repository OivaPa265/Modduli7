# vuodenaika vastuakset
vuodenajat="talvella","keväällä","kesällä","syksyllä"

#kuukausi vastaukset
ajat= "joulukuu","tammikuu","helmikuu","maaliskuu","huhtikuu","toukokuu","kesäkuu","syyskuu","elokuu","lokakuu","marraskuu"

# kykyy käyttäjälä syötteen
syote = int(input("anna numero 1-11 välillä"))

#vähentää yhden numeron syoteestä jotta lista olisi helpompi kutsua numero
kuukaudet =ajat[syote-1]

# vastaukset annetuille numeroille
# tarkistaa annetun numrton ja printaa kuukauden sekä vuoden ajan
if syote in range(1,4):
           print(f"{syote} kuukausi oli {kuukaudet} joka oli {vuodenajat[0]}")

elif syote in range(4,7):
        print(f"{syote} kuukaisi oli {kuukaudet}  joka oli {vuodenajat[1]} ")

elif syote in range(7,9):
        print(f"{syote} kuukausi oli {kuukaudet} joka oli {vuodenajat[2]}")

elif syote in range(9,12):
        print(f"{syote} kuukausi oli {kuukaudet} joka oli {vuodenajat[3]}")





