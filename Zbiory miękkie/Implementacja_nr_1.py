class Spodnie:
    def __init__(self, nazwa, drogie, tanie, jeans, dresowe, klasyczne, modern, fit, granatowe, czarne, na_zamek,
                 na_guziki):
        self.nazwa = nazwa
        self.drogie = drogie
        self.tanie = tanie
        self.jeans = jeans
        self.dresowe = dresowe
        self.klasyczne = klasyczne
        self.modern = modern
        self.fit = fit
        self.granatowe = granatowe
        self.czarne = czarne
        self.na_zamek = na_zamek
        self.na_guziki = na_guziki


dres_adidas = Spodnie("dres_adidas", 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0)
spodnie_pizamowe = Spodnie("spodnie_pizamowe", 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1)
spodnie_do_klubu_studenckiego = Spodnie("spodnie_do_klubu_studenckiego", 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0)
spodnie_do_garnituru = Spodnie("spodnie_do_garnituru", 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0)
zwykly_jeans = Spodnie("zwykly_jeans", 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0)
czarny_jeans = Spodnie("czarny_jeans", 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0)
drogie_spodnie_pizamowe = Spodnie("drogie_spodnie_pizamowe", 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1)
spodnie_do_siadow = Spodnie("spodnie_do_siadow", 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0)
jeans_z_guzikami = Spodnie("jeans_z_guzikami", 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1)

asortyment = [
    dres_adidas, spodnie_pizamowe, spodnie_do_klubu_studenckiego, spodnie_do_garnituru, zwykly_jeans, czarny_jeans,
    drogie_spodnie_pizamowe, spodnie_do_siadow, jeans_z_guzikami]

klient_A = {"jeans": 0.5, "modern": 0.5, "na_zamek": 0.7}
klient_B = {"jeans": 0.5, "klasyczne": 0.5, "granatowe": 0.7,"na_guziki":1}



def znajdz_gacie_dla(zadanie_klienta):
    wagi_klienta = [0] * len(asortyment)
    for x in range(len(asortyment)):
        for parametr in zadanie_klienta:
            wagi_klienta[x] += zadanie_klienta[parametr] * asortyment[x].__getattribute__(parametr)
    print("Wagi klienta " + wagi_klienta.__str__())
    odpowiednie_gacie = asortyment[wagi_klienta.index(max(wagi_klienta))]
    print("Wybrane spodnie to: " + odpowiednie_gacie.nazwa)


znajdz_gacie_dla(klient_A)
znajdz_gacie_dla(klient_B)
