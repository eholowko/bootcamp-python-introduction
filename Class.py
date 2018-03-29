#! /home/kodolamacz/anaconda3/bin/python3.6

import math

class Zespolona:
    def __init__(self,Re,Im):
        self.re = Re
        self.im = Im


def sum_zespolona(licz1,licz2):
    return(licz1.re + licz2.re, licz1.im + licz2.im)


class Row_kwadr:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

def miejsca_zerowe(r):

    delta = r.b * r.b - 4 * r.a * r.c

    if delta < 0:
        return (float("NaN"),float("NaN"))

    delta_sqrt = math.sqrt(delta)

    if r.a == 0:
        if r.b == 0:
            if r.c == 0:
                return(float("Inf"),float("Inf"))
            else:
                return(float("NaN"),float("NaN"))
        else:
            #rownanie liniowe
            x1 = -r.c / r.b
            x2 = x1
    else:
        x1 = -r.b - delta_sqrt / (2 * r.a)
        x2 = -r.b + delta_sqrt / (2 * r.a)

    return(x1,x2)


def main():

    # z1 = Zespolona(3,5)
    # z2 = Zespolona(1,1)

    # (re_sum,im_sum) = sum_zespolona(z1,z2)

    # print("Suma dwóch liczb zespolonych wynosi {0} + {1}i".format(re_sum,im_sum))

    (x1, x2) = miejsca_zerowe(Row_kwadr(0,1,1))

    print("Pierwiastki rownania to {0} i {1}".format(x1,x2))

if __name__ == "__main__":
    main()