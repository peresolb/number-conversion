#!/usr/bin/env python
# coding: utf-8

from cardinal_numbers import *

numberwds_bm = [convert_nums(n) for n in range(1000000)]

numberwds_nn = [convert_nums(n, nn=True) for n in range(1000000)]


def give_nones(nr, nn=False):
    returnlist = []
    for n in range(nr):
        if nn == False:
            if convert_nums(n) is None:
                returnlist.append(n)
        else:
            if convert_nums(n, nn=True) is None:
                returnlist.append(n)
    return returnlist


if __name__ == "__main__":
    nones_bm = give_nones(1000000)

    nones_nn = give_nones(1000000, nn=True)
    print("convert_nums returns None for the following numbers:")
    print(nones_bm)

    print("convert_nums in nn returns None for the following numbers:")
    print(nones_nn)

    reversedfails_bm = [
        numword
        for numword in numberwds_bm
        if convert_nums(numword, reverse=True) is None
    ]

    reversedfails_nn = [
        numword
        for numword in numberwds_nn
        if convert_nums(numword, reverse=True, nn=True) is None
    ]

    print("convert_nums reversed returns None for the following numbers:")
    print(reversedfails_bm)

    print("convert_nums reversed in nn returns None for the following numbers:")
    print(reversedfails_nn)
