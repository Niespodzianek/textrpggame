from mapa import mapa_gry as mapa_gry
class Gracz:
    def __init__(self, pozycja, zdrowie=10, sila=10):
        self.imie = "Bezimienny"
        self.pozycja = pozycja
        self.zdrowie = zdrowie
        self.sila = sila

    def ruch_gracza(self):
        print("Ruch gracza")
        ruch = True
        while ruch:
            kierunek = input("W którym kierunku chcesz się poruszyć: góra, prawo, dół, lewo\n> ")
            if kierunek not in ["góra", "dół", "prawo", "lewo"]:
                print("Zły wybór. Jeszcze raz.")
            else:
                if self.pozycja[kierunek] == 0:
                    print("Koniec mapy. Wybierz jeszcze raz inny kierunek.")
                else:
                    self.pozycja = mapa_gry[self.pozycja[kierunek]]
                    self.sila = self.sila - 1
                    ruch = False

    def __repr__(self):
        return f"<Gracz {self.imie} znajduje się na pozycji {self.pozycja['nazwa']}, ma siłę {self.sila} i zdrowie {self.zdrowie}>"

    def __str__(self):
        return f"Gracz {self.imie} znajduje się na pozycji {self.pozycja['nazwa']}, ma siłę {self.sila} i zdrowie {self.zdrowie}"

# inicjalizacja gry
zawodnik = Gracz(pozycja=mapa_gry[11], zdrowie=12, sila=20)

def program():
    #ruch_gracza()
    print(repr(zawodnik))
    zawodnik.ruch_gracza()
    print(zawodnik)

program()
print("KONIEC PRACY PROGRAMU")

# TODO 1 - kolorowanie literek w oknie terminala
# TODO 2 - poruszanie sie pomiędzy polami mapy - wykonane
