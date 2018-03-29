#! /home/kodolamacz/anaconda3/bin/python3.6


def sortowanie(L):

    is_changed = True
    for i in range(1,len(L)):
        if(not(is_changed)):
            break
        is_changed = False

        for j in range(len(L)-i):
            if(L[j] > L[j+1]):
                is_changed = True
                L[j],L[j+1] = L[j+1],L[j]

    return L

def main():

    list = [i for i in range(10,1,-1)]

    print(sortowanie(list))




if __name__ == "__main__":
    main()