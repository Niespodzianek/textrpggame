from mapa import mapa_gry as mapa_gry
class Gracz:
    def __init__(self, pozycja, zdrowie=0, sila=0):
        self.imie = "Bezimienny"
        self.pozycja = pozycja
        self.zdrowie = zdrowie
        self.sila = sila

    def prezentacja(self):
        print(f"Gracz {self.imie} znajduje się w {self.pozycja['nazwa']}, ma siłę {self.sila} i zdrowie {self.zdrowie}")

# inicjalizacja gry
zawodnik = Gracz(pozycja=mapa_gry[22], zdrowie=12, sila=20)
def ruch_gracza():
    ruch = True
    while ruch:
        zawodnik.prezentacja()
        kierunek = input("W którym kierunku chcesz się poruszyć: góra, prawo, dół, lewo\n> ")
        if kierunek not in ["góra", "dół", "prawo", "lewo"]:
            print("Zły wybór ruchu. Jeszcze raz.")
        else:
            if zawodnik.pozycja[kierunek] == 0:
                print("Koniec mapy. Wybierz jeszcze raz inny kierunek.")
            else:
                zawodnik.pozycja = mapa_gry[zawodnik.pozycja[kierunek]]
                zawodnik.sila = zawodnik.sila - 0.5
                ruch = False
    zawodnik.prezentacja()

def program():
    ruch_gracza()

program()
print("KONIEC PRACY PROGRAMU")

# TODO 1 - kolorowanie literek w oknie terminala
# TODO 2 - poruszanie sie pomiędzy polami mapy
