class Warzywo:
    def __init__(self, nazwa, świeże, mrożone, ostre, słodkie, zielone, czerwone, lokalne, tropikalne, liściaste,
                 bulwowe):
        self.nazwa = nazwa
        self.świeże = świeże
        self.mrożone = mrożone
        self.ostre = ostre
        self.słodkie = słodkie
        self.zielone = zielone
        self.czerwone = czerwone
        self.lokalne = lokalne
        self.tropikalne = tropikalne
        self.liściaste = liściaste
        self.bulwowe = bulwowe


papryka = Warzywo("papryka", 1, 0, 1, 0, 1, 1, 0, 0, 0, 0)
jablko = Warzywo("jablko", 1, 0, 0, 1, 1, 1, 1, 0, 1, 0)
szpinak = Warzywo("szpinak", 0, 1, 0, 0, 1, 0, 0, 0, 0, 1)
pietruszka = Warzywo("pietruszka", 1, 0, 0, 0, 0, 0, 1, 0, 0, 1)
pitaja = Warzywo("pitaja", 1, 0, 1, 0, 0, 1, 0, 1, 1, 0)

asortyment = [papryka, jablko, szpinak, pietruszka, pitaja]

klient_A = {"świeże": 0.5, "zielone": 0.7, "ostre": 1}
klient_B = {"mrożone": 0.3, "zielone": 0.5, "słodkie": 0.2, "liściaste": 0.1}
klient_C = {"świeże": 1, "zielone": 0.5, "czerwone": 0.5, "słodkie": 0.5}


def znajdz_warzywo_dla(zadanie_klienta):
    wagi_klienta = [0] * len(asortyment)
    for x in range(len(asortyment)):
        for parametr in zadanie_klienta:
            wagi_klienta[x] += zadanie_klienta[parametr] * asortyment[x].__getattribute__(parametr)
    print("Wagi klienta " + wagi_klienta.__str__())
    odpowiednie_warzywo = asortyment[wagi_klienta.index(max(wagi_klienta))]
    print("Wybrane warzywo to: " + odpowiednie_warzywo.nazwa)


znajdz_warzywo_dla(klient_A)
znajdz_warzywo_dla(klient_B)
znajdz_warzywo_dla(klient_C)
