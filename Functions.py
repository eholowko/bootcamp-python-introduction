#! /home/kodolamacz/anaconda3/bin/python3.6


def Sortowanie_zliczanie(L,a,b):

    max_index = 0

    size = b - a

    print(L, end=" ")
    print()


    hist = [0 for i in range(size + 1)]

    for el in L:
        hist[el - a] += 1

    print(hist, end=" ")
    print()

    new_L = [0 for i in range(size)]

    index = 0
    for i,value in enumerate(hist):
        for j in range(value):
            new_L[index + j] = a + i
        index += value

    print(new_L, end=" ")
    print()

    for i,value in enumerate(hist):
        if hist[max_index] < value:
            max_index = i

    return max_index


def main():


    L = [2,3,5,6,3,6,7,1,8,-4,-4,-4,5,0,0]
    a = -5
    b = 10
    index = Sortowanie_zliczanie(L,a,b)

    print("Najwiekszy indeks = {}".format(index))
    print("W liscie jest najwiecej {}".format(a + index))

if __name__ == "__main__":
    main()