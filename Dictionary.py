#! /home/kodolamacz/anaconda3/bin/python3.6


def Sortowanie_zliczanie(L,a,b):

    size = b - a

    print(L, end=" ")
    print()


    dict = {}

    for el in L:
        if (el) not in dict:
            dict[el] = 1
        else:
            dict[el] += 1
        # dict[el] = dict.get(el,0) + 1


    print(dict)
    # print()


    new_L = [0 for i in range(size)]

    index = 0

    for el in L:
        if el in dict.keys():
            for j in range(dict[el]):
                new_L[index+j] = el


    print(new_L, end=" ")
    print()


    max_elem = 0
    max_count = 0

    for key, value in dict.items():
        if value > max_count:
            max_elem =key
            max_count = value

    return (max_count,max_elem)


def main():


    L = [2,3,5,6,3,6,7,1,8,-4,-4,-4,5,0,0]
    a = -5
    b = 10
    (index,value) = Sortowanie_zliczanie(L,a,b)

    print("Najwiekszy indeks = {}".format(index))
    print("W liscie jest najwiecej {}".format(value))

if __name__ == "__main__":
    main()