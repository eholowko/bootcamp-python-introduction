#! /home/kodolamacz/anaconda3/bin/python3.6

def pot(podstawa,wykladnik):
    return podstawa ** wykladnik

def silnia(n):
    if n == 0 or n == 1:
        return 1
    return(n * silnia(n-1))

def main():

    print(silnia(5))

    # print("wynik {0} do potegi {1}  = {2}".format(2,3,pot(2,3)))

if __name__ == "__main__":
    main()