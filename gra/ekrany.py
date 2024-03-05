SZEROKOSC = 160
WYSOKOSC = 50

def ekran(wypelniacz=" "):
    zawartosc = wypelniacz
    print(SZEROKOSC * "*")
    for number in range(WYSOKOSC):
        print("*" + ((SZEROKOSC - 2) * zawartosc) + "*")
    print(SZEROKOSC * "*")

if __name__ == 'main':
    ekran()

ekran()

