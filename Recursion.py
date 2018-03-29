#! /home/kodolamacz/anaconda3/bin/python3.6

def potegowanie(podstawa,wykladnik):
    #zlozonosc log(wykladnik)
    if wykladnik == 0:
        return 1
    if wykladnik == 1:
        return podstawa

    wynik = 0

    if wykladnik % 2 == 0:
        pot = potegowanie(podstawa, wykladnik / 2)
        wynik = pot * pot
    else:
        pot = potegowanie(podstawa,wykladnik//2)
        wynik = pot * pot * podstawa

    return(wynik)



def silnia(n):
    if n == 0 or n == 1:
        return 1
    return(n * silnia(n-1))


def main():
    print(potegowanie(2,5))

if __name__ == "__main__":
    main()