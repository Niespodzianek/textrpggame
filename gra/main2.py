class Gracz:
    def __init__(self, pozycja, zdrowie = 0, sila = 0):
        self.pozycja = pozycja
        self.zdrowie = zdrowie
        self.sila = sila

mapa_gry = {
    11:{},
    12:{},
    13:{},
    14:{},
    21:{},
    22:{
        "nazwa": "start"
    },
    23:{},
    24:{},
    31:{},
    32:{},
    33:{},
    34:{},
    41:{},
    42:{},
    43:{},
    44:{}
    }

zawodnik = Gracz("start")

def program():
    print(zawodnik)
    
    # logika
    ruch = input("Jaki wybierasz ruch: góra, w prawo, w lewo, dół")
    if ruch is ["góra", "prawo", "lewo", "dół"]:
        print("Ruszas się")
    else:
        print("Zły wybór ruchu")
    
    print("KONIEC PRACY PRORAMU")

program()

#TODO 1 - kolorowanie literek w oknie terminala
#TODO 2 - poruszanie sie pomiędzy polami mapy
