import random

def rzut_kostka():
    licznik = 0
    wylosowane_liczby = []
    liczba_rzutow = 3
    while licznik < liczba_rzutow:
        licznik = licznik + 1
        losowa_liczba = random.randrange(1, 7)
        print(losowa_liczba)
        wylosowane_liczby.append(losowa_liczba)
    print(f"Wylosowane liczby: {wylosowane_liczby}")

if __name__ == 'main':
    rzut_kostka()

rzut_kostka()

