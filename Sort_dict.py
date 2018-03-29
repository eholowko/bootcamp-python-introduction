#! /home/kodolamacz/anaconda3/bin/python3.6


class uczen:

    def __init__(self,nazwisko,srednia):
        self.nazwisko = nazwisko
        self.srednia = srednia

def sort_dict(dict):

    L = [key for key in dict.keys()]

    print(L,end = " ")
    print()

    is_changed = True
    for i in range(1,len(L)):
        if(not(is_changed)):
            break
        is_changed = False

        for j in range(len(L)-i):
            if(dict[L[j]] > dict[L[j+1]]):
                is_changed = True
                L[j],L[j+1] = L[j+1],L[j]

    return L

def main():

    S = {uczen("Kowalski",3.4),uczen("Nowak",4.4),uczen("Xyz",3.5),uczen("Pod",4.56)}

    dictionary = {s.nazwisko:s.srednia for s in S}
    print(dictionary)

    dict = {'Kowalski':3.4,"Nowak":4.4, "Xyz": 3.5,"Pod":4.56}

    print(sort_dict(dict))


if __name__ == "__main__":
    main()