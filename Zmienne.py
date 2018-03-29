#! /home/kodolamacz/anaconda3/bin/python3.6
def main():
    print("Podaj liczbę schodów")
    stairs = int(input())

    floor = 0

    floor = stairs//15
    on_floor = False


    if stairs % 15 == 0:
        on_floor = True
        print("Jesteś na " + str(floor) + " piętrze")
    else:
        on_floor = False
        print("Jesteś między " + str(floor) + " a " + str(floor +1) + " piętrem")

    if floor % 2 == 0 and on_floor:
        print("Toaleta jest tuż obok")
    else:
        if(stairs % 15 == 0):
            print("Mozesz iść albo na góre albo na dół")
        else:
            floor_up = floor + 1
            floor_down = floor - 1

            print("Wyższe " + str(floor_up))
            print("NIższe " + str (floor_down))

            stairs_up = abs(((floor_up * 15)- stairs))
            stairs_down = abs(((floor_down * 15) -  stairs))

            print("Schody do góry " + str(stairs_up))
            print("Schody do dołu " + str(stairs_down))
            if(stairs_up < stairs_down):
                print("Idż piętro wyżej. Masz do przejścia " + str(stairs_up))
            else:
                print("Idź piętro niżej. Masz do przejścia " + str(stairs_down))



if __name__ == "__main__":
    main()