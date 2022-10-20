#!/usr/bin/env python
# coding: utf-8

from cardinal_numbers import convert_nums

b_ordinals_bm = {
    1: "første",
    2: "andre",
    3: "tredje",
    4: "fjerde",
    5: "femte",
    6: "sjette",
    7: "sjuende",
    8: "åttende",
    9: "niende",
}

b_ordinals_nn = {
    1: "første",
    2: "andre",
    3: "tredje",
    4: "fjerde",
    5: "femte",
    6: "sjette",
    7: "sjuande",
    8: "åttande",
    9: "niande",
}

# 11.-19.
t_ordinals_bm = {
    11: "ellevte",
    12: "tolvte",
    13: "trettende",
    14: "fjortende",
    15: "femtende",
    16: "sekstende",
    17: "syttende",
    18: "attende",
    19: "nittende",
}
t_ordinals_nn = {
    11: "ellevte",
    12: "tolvte",
    13: "trettande",
    14: "fjortande",
    15: "femtande",
    16: "sekstande",
    17: "syttande",
    18: "attende",
    19: "nittande",
}

# 20, 30, 40 50, 60, 70, 80, 90
do_ordinals_bm = {
    20: "tjuende",
    30: "trettiende",
    40: "førtiende",
    50: "femtiende",
    60: "sekstiende",
    70: "syttiende",
    80: "åttiende",
    90: "nittiende",
}
do_ordinals_nn = {
    20: "tjuande",
    30: "trettiande",
    40: "førtiande",
    50: "femtiande",
    60: "sekstiande",
    70: "syttiande",
    80: "åttiande",
    90: "nittiande",
}


# High primitives
high_ordinals = {100: "hundrede", 1000: "tusende"}
high_ordinals_rev = {"hundrede": 100, "tusende": 1000}


def _ordinals_to_nn(ordinal, nn=False):
    """Ordinals 1-99 int to string. Reverse in separate func calling on this func. Parsing and returning strings of the type "9." will be the task of a higher func"""
    if type(ordinal) is int:
        if ordinal < 10 and ordinal != 0:
            if nn == False:
                return b_ordinals_bm[ordinal]
            else:
                return b_ordinals_nn[ordinal]
        elif ordinal == 10:
            if nn == False:
                return "tiende"
            else:
                return "tiande"
        elif nn == False and ordinal in do_ordinals_bm.keys():
            return do_ordinals_bm[ordinal]
        elif nn == True and ordinal in do_ordinals_nn.keys():
            return do_ordinals_nn[ordinal]
        elif nn == False and ordinal in t_ordinals_bm.keys():
            return t_ordinals_bm[ordinal]
        elif nn == True and ordinal in t_ordinals_nn.keys():
            return t_ordinals_nn[ordinal]
        elif len(str(ordinal)) == 2 and ordinal > 19:  # 43
            numstring = str(ordinal)
            firstdig = int(numstring[0]) * 10  # 40
            seconddig = int(numstring[1])  # 4
            if nn == False:
                firststring = convert_nums(firstdig)  # førti
                secondstring = b_ordinals_bm[seconddig]  # tredje
                return "%s%s" % (firststring, secondstring)
            else:
                firststring = convert_nums(firstdig, nn=True)  # førti
                secondstring = b_ordinals_nn[seconddig]  # tredje
                return "%s%s" % (firststring, secondstring)


def ordinals_to_nn_rev(ordinal, nn=False):
    if nn == False:
        ordinalsdict_bm = {}
        for n in range(100):
            if n > 0:
                ordinalsdict_bm[_ordinals_to_nn(n)] = n
        if type(ordinal) is str and ordinal in ordinalsdict_bm.keys():
            return ordinalsdict_bm[ordinal]
    else:
        ordinalsdict_nn = {}
        for n in range(100):
            if n > 0:
                ordinalsdict_nn[_ordinals_to_nn(n, nn=True)] = n
        if type(ordinal) is str and ordinal in ordinalsdict_nn.keys():
            return ordinalsdict_nn[ordinal]


def _ordinal_to_cardinal(ordinal, nn=False):
    """Helper func. Convert one word ordinal written as str to cardinal written as str"""
    if type(ordinals_to_nn_rev(ordinal)) is int and nn == False:
        myint = ordinals_to_nn_rev(ordinal)
        return convert_nums(myint)
    elif type(ordinals_to_nn_rev(ordinal, nn=True)) is int and nn == True:
        myint = ordinals_to_nn_rev(ordinal, nn=True)
        return convert_nums(myint, nn=True)
    elif ordinal in high_ordinals_rev.keys():
        myint = high_ordinals_rev[ordinal]
        hundre_or_tusen = convert_nums(myint).split(" ")[
            -1
        ]  # to avoid "ett" in "ett tusen"
        return hundre_or_tusen


def convert_ords(ordinal, reverse=False, nn=False):
    if reverse == False:
        if type(ordinal) is int and ordinal != 0 and ordinal < 1000000:
            if type(_ordinals_to_nn(ordinal, nn=False)) is str and nn == False:  # 1-99
                return _ordinals_to_nn(ordinal, nn=False)
            elif type(_ordinals_to_nn(ordinal, nn=True)) is str and nn == True:  # 1-99
                return _ordinals_to_nn(ordinal, nn=True)
            elif ordinal in high_ordinals.keys():  # 100 1000
                return high_ordinals[ordinal]
            else:  # 144
                numerallist = []  # ['hundre', 'og', 'førtifire']
                if nn == False:
                    numerallist = convert_nums(ordinal).split(" ")
                else:
                    numerallist = convert_nums(ordinal, nn=True).split(" ")
                lastword = numerallist[-1]  # førtifire
                restlist = numerallist[:-1]  # ['hundre', 'og']
                reststring = " ".join(restlist)
                lastord = ""
                if nn == False:
                    lastnum = convert_nums(lastword, reverse=True)
                    if lastnum < 100:
                        lastord = _ordinals_to_nn(lastnum)
                    elif lastnum in high_ordinals.keys():
                        lastord = high_ordinals[lastnum]
                    else:
                        return None
                else:
                    lastnum = convert_nums(lastword, reverse=True, nn=True)
                    if lastnum < 100:
                        lastord = _ordinals_to_nn(lastnum, nn=True)
                    elif lastnum in high_ordinals.keys():
                        lastord = high_ordinals[lastnum]
                    else:
                        return None
                ordstring = "%s %s" % (reststring, lastord)
                return ordstring
    else:
        if not type(ordinal) is str:
            return None
        if nn == False and type(ordinals_to_nn_rev(ordinal)) is int:
            return ordinals_to_nn_rev(ordinal)
        elif nn == True and type(ordinals_to_nn_rev(ordinal, nn=True)) is int:
            return ordinals_to_nn_rev(ordinal, nn=True)
        elif ordinal in high_ordinals_rev:
            return high_ordinals_rev[ordinal]
        elif len(ordinal.split(" ")) > 1:
            wdlist = ordinal.split(" ")  # to, hundre, tusen, og, sjuande
            tailstr = wdlist[-1]  # sjuande
            headstr = " ".join(wdlist[:-1])  # to hundre tusen og
            if type(_ordinal_to_cardinal(tailstr)) is str and nn == False:
                cardinaltail = _ordinal_to_cardinal(tailstr)
                cardinalstr = "%s %s" % (headstr, cardinaltail)
                if type(convert_nums(cardinalstr, reverse=True)) is int:
                    return convert_nums(cardinalstr, reverse=True)
                else:
                    return None
            elif type(_ordinal_to_cardinal(tailstr, nn=True)) is str and nn == True:
                cardinaltail = _ordinal_to_cardinal(tailstr, nn=True)
                cardinalstr = "%s %s" % (headstr, cardinaltail)
                if type(convert_nums(cardinalstr, reverse=True, nn=True)) is int:
                    return convert_nums(cardinalstr, reverse=True, nn=True)
                else:
                    return None
            else:
                return None
        else:
            return None


if __name__ == "__main__":
    # testing
    mydigit = 243564
    mynumstring = "hundre og tredje"
    mydigit_nn = 34388
    mynumstring_nn = "åttisjuande"

    print(
        "Digit conversion bm: %s\nString conversion bm: %s"
        % (convert_ords(mydigit), convert_ords(mynumstring, reverse=True))
    )
    print(
        "Digit conversion nn: %s\nString conversion nn: %s"
        % (
            convert_ords(mydigit_nn, nn=True),
            convert_ords(mynumstring_nn, nn=True, reverse=True),
        )
    )
