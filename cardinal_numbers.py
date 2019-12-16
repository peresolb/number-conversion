#!/usr/bin/env python
# coding: utf-8

import sys
import os
import nltk


# Dict for basic primitive numbers: 1-10
b = {1: 'én', 2: 'to', 3: 'tre', 4: 'fire', 5: 'fem', 6: 'seks', 7: 'sju', 8: 'åtte', 9: 'ni', 10: 'ti'}
b_nn = {1: 'ein', 2: 'to', 3: 'tre', 4: 'fire', 5: 'fem', 6: 'seks', 7: 'sju', 8: 'åtte', 9: 'ni', 10: 'ti'}

# Dict for teen primitive numbers: 11-19
t = {11: 'elleve', 12: 'tolv', 13: 'tretten', 14: 'fjorten', 15: 'femten',
     16: 'seksten', 17: 'sytten', 18: 'atten', 19: 'nitten'}


# Dict for two digit primitive numbers: 20-90
do = {20: 'tjue', 30: 'tretti', 40: 'førti', 50: 'femti', 60: 'seksti', 70: 'sytti', 80: 'åtti', 90: 'nitti'}


# Dict for the 3 digit primitive number: 100
doo = {100: 'hundre'}


# Dict for the 4 digit primitive number: 1000
dooo = {1000: 'tusen'}



# Reverser function for primitive number dicts
def _revdict(numberdict):
    newdict = {}
    for k, v in numberdict.items():
        newdict[v] = k
    return newdict


# The reverse of the primitive number dicts, where strings are keys and integers are values,
# are name of original dict underscore 'r'
b_r, b_nn_r, t_r, do_r, doo_r, dooo_r = _revdict(b), _revdict(b_nn), _revdict(t), _revdict(do), _revdict(doo), _revdict(dooo)


def _oneten(nr, reverse=False, nn=False):
    """Function taking an int from 1-10 and returning the corresponding word,
    or, if reverse=True, taking a numberword from 1-10 and returning the digit"""
    if reverse == False:
        if not type(nr) is int:
            return None
        if nr <= 10:
            if nn == False:
                return b[nr]
            else:
                 return b_nn[nr]
    else:
        if not type(nr) is str:
            return None
        if nn == False:
            if nr in b_r.keys():
                return b_r[nr]
        else:
             if nr in b_nn_r.keys():
                return b_nn_r[nr]


def _onedig(nr, reverse=False, nn=False):
    if reverse == False:
        if not _oneten(nr) == 'ti':
            if nn == False:
                return _oneten(nr)
            else:
                return _oneten(nr, nn=True)
    if reverse == True:
        if not _oneten(nr, reverse=True) == 10:
            if nn == False:
                return _oneten(nr, reverse=True)
            else:
                return _oneten(nr, reverse=True, nn=True)


def _teen(nr, reverse=False):
    """Function taking a primitive two-digit int in the teen range and returning the
    corresponding word, or, if reverse=True, the corresponding number word"""
    if reverse == False:
        if not type(nr) is int:
            return None
        if nr in t.keys():
            return t[nr]
    else:
        if not type(nr) is str:
            return None
        if nr in t_r.keys():
            return t_r[nr]


def _twodig(nr, reverse=False):
    """Function taking a primitive two-digit int in the range 20-90 and returning 
    the corresponding word, or, if reverse=True, the corresponding number word"""    
    if reverse == False:
        if not type(nr) is int:
            return None
        if nr in do.keys():
            return do[nr]
    else:
        if not type(nr) is str:
            return None
        if nr in do_r.keys():
            return do_r[nr]


def _numparser(numword, nn=False):
    """Parse word to see if they start with a wd in firstnumwords.
    If yes, return firstnumword and second part"""
    if not type(numword) is str:
        return None
    firstpart = ''
    scndpart = ''
    firstnumwords = list(do_r.keys())
    for s in firstnumwords:
        if numword.startswith(s):
            slength = len(s)
            firstpart = s
            scndpart = numword[slength:]
            if nn == False:
                if scndpart in b_r.keys() and b_r[scndpart] < 10: #Only return if second part is dig below 10
                    return (firstpart, scndpart)
            else:
                if scndpart in b_nn_r.keys() and b_nn_r[scndpart] < 10: #Only return if second part is dig below 10
                    return (firstpart, scndpart)



def _one_to_nineteen(nr, reverse=False, nn=False):
    """Function taking a primitive two-digit int in the range 1-19 
    and returning the corresponding word, or, if reverse=True, the corresponding number word"""
    if reverse == False:
        if not type(nr) is int:
            return None
        if nr < 11:
            if nn == False:
                return _oneten(nr)
            else:
                return _oneten(nr, nn=True)
        elif nr < 20:
            return _teen(nr)
    else:
        if not type(nr) is str:
            return None
        if nn == False:
            if type(_oneten(nr, reverse=True)) is int:
                return _oneten(nr, reverse=True)
            elif type(_teen(nr, reverse=True)):
                return _teen(nr, reverse=True)
        else:
            if type(_oneten(nr, reverse=True, nn=True)) is int:
                return _oneten(nr, reverse=True, nn=True)
            elif type(_teen(nr, reverse=True)):
                return _teen(nr, reverse=True)



def _one_to_nn(nr, reverse= False, nn=False):
    """Function taking an int in the range 1-99 and returning the corresponding word. Reverse as before"""
    if reverse == False:
        if not type(nr) is int:
            return None
        if nr > 0:
            if nr < 20:
                if nn == False:
                    return _one_to_nineteen(nr)
                else:
                    return _one_to_nineteen(nr, nn=True)
            elif nr < 100:
                if nr in do.keys():
                    return _twodig(nr)
                else:
                    nrstring = str(nr)
                    frstdig = int(nrstring[0])*10
                    scndig = int(nrstring[1])
                    frstwd = _twodig(frstdig)
                    if nn == False:
                        scnwd = _onedig(scndig)
                    else:
                        scnwd = _onedig(scndig, nn=True)
                    nrwd = frstwd+scnwd
                    return nrwd
    else:
        if not type(nr) is str:
            return None
        if nn == False:
            if type(_one_to_nineteen(nr, reverse=True)) is int:
                return _one_to_nineteen(nr, reverse=True)
            elif type(_twodig(nr, reverse=True)) is int:
                return _twodig(nr, reverse=True)
            else:
                if _numparser(nr) == None:
                    return None
                parsed = _numparser(nr)
                first = _twodig(parsed[0], reverse=True)
                second = _one_to_nineteen(parsed[1], reverse=True)
                return first+second
        else:
            if type(_one_to_nineteen(nr, reverse=True, nn=True)) is int:
                return _one_to_nineteen(nr, reverse=True, nn=True)
            elif type(_twodig(nr, reverse=True)) is int:
                return _twodig(nr, reverse=True)
            else:
                if _numparser(nr, nn=True) == None:
                    return None
                parsed = _numparser(nr, nn=True)
                first = _twodig(parsed[0], reverse=True)
                second = _one_to_nineteen(parsed[1], reverse=True, nn=True)
                return first+second


def _one_to_nnn(nr, reverse= False, nn=False):
    """Function taking an int in the range 1-999 and returning the corresponding word. Reverse as before"""
    if reverse == False:
        if not type(nr) is int:
            return None
        if nr == 0:
            return None
        if nr < 100: #1-99
            if nn == False:
                return _one_to_nn(nr)
            else:
                return _one_to_nn(nr, nn=True) 
        elif nr < 1000:
            if nr is 100: #100
                return doo[100]
            else:
                nrstring = str(nr) #435 181
                frstdig = int(nrstring[0]) #4 1 
                scndig = int(nrstring[1]) #3 8
                thrdig = int(nrstring[2]) #5 1 
                scthdig = int(nrstring[1:]) #35 81
                if nn == False:
                    frstwd = _onedig(frstdig) # fire
                else:
                    frstwd = _onedig(frstdig, nn=True)
                nrwd = ''
                if scndig == 0: #405 or 400
                    if thrdig == 0: #400
                        nrwd = "%s %s" % (frstwd, doo[100]) #fire hundre
                    else: #405
                        if nn == False:
                            thrdwd = _one_to_nn(thrdig) # fem
                        else:
                            thrdwd = _one_to_nn(thrdig, nn=True)
                        if frstdig != 1:
                            nrwd = "%s %s og %s" % (frstwd, doo[100], thrdwd) #fire hundre og fem
                        else:
                            nrwd = "%s og %s" % (doo[100], thrdwd) #hundre og fem
                else: #435
                    scthwd = ''
                    if nn == False:
                        scthwd = _one_to_nn(scthdig) #trettifem
                    else:
                        scthwd = _one_to_nn(scthdig, nn=True)
                    if frstdig != 1:
                        nrwd = "%s %s og %s" % (frstwd, doo[100], scthwd)
                    else:
                        nrwd = "%s og %s" % (doo[100], scthwd) # hundre og trettifem
                return nrwd
    else:
        if not type(nr) is str:
            return None
        if type(doo_r.get(nr, None)) is int: #hundre - 100
            return doo_r[nr]
        elif len(nr.split(' ')) == 1 and type(_one_to_nn(nr, reverse=True)) is int and nn == False:
            return _one_to_nn(nr, reverse=True) #44
        elif len(nr.split(' ')) == 1 and type(_one_to_nn(nr, reverse=True, nn=True)) is int and nn == True:
            return _one_to_nn(nr, reverse=True, nn=True) #44
        elif len(nr.split(' ')) == 2: #to hundre
                splitwords = nr.split(' ')
                if nn == False and nr == 'ett hundre':
                    return 100
                elif nn == True and nr == 'eitt hundre':
                    return 100
                elif type(_one_to_nn(splitwords[0], reverse=True)) is int and splitwords[1] == 'hundre':
                    return _one_to_nn(splitwords[0], reverse=True)*100
        elif len(nr.split(' ')) == 3: #hundre og tre
            splitwords = nr.split(' ')
            if splitwords[0] == 'hundre' and splitwords[1] == 'og':
                if nn == False:
                    if type(_one_to_nn(splitwords[2], reverse=True)) is int:
                        return 100+_one_to_nn(splitwords[2], reverse=True)
                else:
                    if type(_one_to_nn(splitwords[2], reverse=True, nn=True)) is int:
                        return 100+_one_to_nn(splitwords[2], reverse=True, nn=True)
            else:
                return None
        elif len(nr.split(' ')) == 4: #ett hundre og trettifire, fire hundre og åtte
            splitwords = nr.split(' ')
            if nn == False:
                if splitwords[0] == 'ett' and splitwords[1] == 'hundre' and splitwords[2] == 'og' and \
                type(_one_to_nn(splitwords[3], reverse=True)) is int: #ett hundre og trettifire
                    return 100+_one_to_nn(splitwords[3], reverse=True)
                elif type(_one_to_nn(splitwords[0], reverse=True)) is int and \
                _one_to_nn(splitwords[0], reverse=True) < 10 and splitwords[1] == 'hundre' and \
                splitwords[2] == 'og' and type(_one_to_nn(splitwords[3], reverse=True)) is int: #fire hundre og trettifire
                    hundreds = _one_to_nn(splitwords[0], reverse=True)*100
                    tens = _one_to_nn(splitwords[3], reverse=True)
                    return hundreds+tens
                else:
                    return None
            else:
                if splitwords[0] == 'eitt' and splitwords[1] == 'hundre' and splitwords[2] == 'og' \
                and type(_one_to_nn(splitwords[3], reverse=True, nn=True)) is int: #eit hundre og trettifire
                    return 100+_one_to_nn(splitwords[3], reverse=True, nn=True)
                elif type(_one_to_nn(splitwords[0], reverse=True, nn=True)) is int and \
                _one_to_nn(splitwords[0], reverse=True, nn=True) < 10 and \
                splitwords[1] == 'hundre' and splitwords[2] == 'og' and \
                type(_one_to_nn(splitwords[3], reverse=True, nn=True)) is int: #fire hundre og trettifire
                    hundreds = _one_to_nn(splitwords[0], reverse=True, nn=True)*100
                    tens = _one_to_nn(splitwords[3], reverse=True, nn=True)
                    return hundreds+tens
                else:
                    return None


def _high_hundred(nr, nn=False):
    """In Norwegian, as in English, it is possible to express the numbers 1100-1999 with hundreds,
    e.g. "tolv hundre og nittiåtte", /twelve hundred and ninety-eight/. We want to be able to convert 
    these to integers. However, we don't need to produce them, so this algoritm only goes from strings to integers"""
    if not type(nr) is str:
        return None
    if len(nr.split(' ')) > 1:
        frstwd = nr.split(' ')[0]
        if not type(_teen(frstwd, reverse = True)) is int:
            return None
        frstdig = _teen(frstwd, reverse = True)
        if len(nr.split(' ')) == 2 and nr.split(' ')[1] == 'hundre': # femten hundre
            return frstdig*100
        elif len(nr.split(' ')) == 4 and nr.split(' ')[1] == 'hundre' and nr.split(' ')[2] == 'og':
            if nn == False and type(_one_to_nn(nr.split(' ')[3], reverse=True)) is int: # femten hundre og førtito
                lastdigs = _one_to_nn(nr.split(' ')[3], reverse = True)
                return (frstdig*100)+lastdigs
            elif nn == True and type(_one_to_nn(nr.split(' ')[3], reverse=True, nn=True)) is int: # femten hundre og førtito
                lastdigs = _one_to_nn(nr.split(' ')[3], reverse = True, nn=True)
                return (frstdig*100)+lastdigs


def _one_to_nnnnnn(nr, reverse=False, nn=False):
    """Function taking an int in the range 1-999999 and returning the corresponding word. Reverse as before"""
    if reverse == False:
        if not type(nr) is int:
            return None
        if nr == 0:
            return None
        if nr < 1000: #1-999
            if nn == False:
                return _one_to_nnn(nr)
            else:
                return _one_to_nnn(nr, nn=True)
        elif nr < 1000000: #1000-999999
            if nr == 1000: #1000
                if nn == False:
                    return 'ett tusen'
                else:
                    return 'eitt tusen'
            else:
                nrstring = str(nr) #Starting with last three digits. e.g. 23[456]
                ultdig = int(nrstring[-1]) #6
                penultdig = int(nrstring[-2]) #5
                antepenultdig = int(nrstring[-3]) #4
                ult_and_penultdig = int(nrstring[-2:]) #56
                ult_penult_antepenultdig = int(nrstring[-3:]) #456
                tailstring = ''
                if antepenultdig == 0: # 012, 002, 000
                    if penultdig == 0: # 000, 002
                        if ultdig == 0: # 000
                            tailstring = 'tusen'
                        else: # 002
                            if nn == False:
                                ultstring = _one_to_nnn(ultdig)
                                tailstring = "tusen og %s" % ultstring # tusen og to
                            else:
                                ultstring = _one_to_nnn(ultdig, nn=True)
                                tailstring = "tusen og %s" % ultstring # tusen og to
                    else: # 012
                        if nn == False:
                            ult_and_penultstring = _one_to_nnn(ult_and_penultdig)
                            tailstring = "tusen og %s" % ult_and_penultstring # tusen og tolv
                        else:
                            ult_and_penultstring = _one_to_nnn(ult_and_penultdig, nn=True)
                            tailstring = "tusen og %s" % ult_and_penultstring # tusen og tolv
                else: # 456
                    if nn == False:
                        ult_penult_antepenultstring = _one_to_nnn(ult_penult_antepenultdig)
                        if str(ult_penult_antepenultdig)[0] == '1':
                            tailstring = "tusen ett %s" % ult_penult_antepenultstring # tusen ett hundre
                        else:
                            tailstring = "tusen %s" % ult_penult_antepenultstring # tusen fire hundre og femtiseks
                    else:
                        ult_penult_antepenultstring = _one_to_nnn(ult_penult_antepenultdig, nn=True)
                        if str(ult_penult_antepenultdig)[0] == '1':
                            tailstring = "tusen eitt %s" % ult_penult_antepenultstring # tusen ett hundre
                        else:
                            tailstring = "tusen %s" % ult_penult_antepenultstring # tusen fire hundre og femtiseks
                startdigs = int(nrstring[:-3])  # startstring can consist of the 1, 2 or 3 first digits
                startstring = ''
                if startdigs == 1: #1001 starts with "ett"
                    if nn == False:
                        startstring = 'ett'
                    else:
                        startstring = 'eitt'
                elif startdigs > 99 and startdigs < 200: #155555 starts with ett
                    if nn == False:
                        startnumstring = _one_to_nnn(startdigs)
                        startstring = "ett %s" % startnumstring
                    else:
                        startnumstring = _one_to_nnn(startdigs, nn=True)
                        startstring = "eitt %s" % startnumstring
                else: #the remaining numbers are purely compositional
                    if nn == False:
                        startstring = _one_to_nnn(startdigs)
                    else:
                        startstring = _one_to_nnn(startdigs, nn=True)
                numstring = "%s %s" % (startstring, tailstring)
                return numstring
    else:
        if not type(nr) is str:
            return None
        if type(_one_to_nnn(nr, reverse=True)) is int and nn == False:
            return _one_to_nnn(nr, reverse=True) #444
        elif type(_one_to_nnn(nr, reverse=True, nn=True)) is int and nn == True:
            return _one_to_nnn(nr, reverse=True, nn=True) #444
        elif nr == 'tusen': #tusen - 1000
            return 1000
        elif len(nr.split(' ')) > 1 and nr.split(' ')[-1] == 'tusen': # ett tusen, ett hundre tusen etc.
            wdlist = nr.split(' ')
            firstphrase = ' '.join(wdlist[:-1])
            if type(_one_to_nnn(firstphrase, reverse=True)) is int and nn == False:
                    firstdig = _one_to_nnn(firstphrase, reverse=True)
                    return firstdig*1000
            elif type(_one_to_nnn(firstphrase, reverse=True, nn=True)) is int and nn == True:
                firstdig = _one_to_nnn(firstphrase, reverse=True, nn=True)
                return firstdig*1000
            elif len(nr.split(' ')) == 2 and nr.split(' ')[0] == "ett" and nn == False: # ett tusen
                return 1000
            elif len(nr.split(' ')) == 2 and nr.split(' ')[0] == "eitt" and nn == True:
                return 1000
            else: # misspellings should not result in return value
                return None
        else:
            if len(nr.split(' ')) > 1: # all other numbers should contain spaces
                numwordlist = nr.split(' ')
                if 'tusen' in numwordlist: # Find last part of numphrase, which starts with "tusen"
                    tusenind = numwordlist.index('tusen') #find index of "tusen"
                    lastwords = numwordlist[tusenind:] # words from 'tusen'
                    firstwords = numwordlist[:tusenind] # words until 'tusen'
                    lastdigs = 0
                    if len(lastwords) == 3:
                        if lastwords[1] == 'og': # 'tusen og fire' 'tusen og førtifire'
                            lastword = lastwords[-1]
                            if nn == False:
                                lastdigs = _one_to_nnn(lastword, reverse=True)
                            elif nn == True:
                                lastdigs = _one_to_nnn(lastword, reverse=True, nn=True)
                        elif nn == False and type(_one_to_nnn(' '.join(lastwords[1:]), reverse=True)) is int \
                        and lastwords[2] == 'hundre': #tusen to hundre
                            hundredphrase = ' '.join(lastwords[1:])
                            lastdigs = _one_to_nnn(hundredphrase, reverse=True)
                        elif nn == True and type(_one_to_nnn(' '.join(lastwords[1:]), reverse=True, nn=True)) is int \
                        and lastwords[2] == 'hundre': #tusen to hundre
                            hundredphrase = ' '.join(lastwords[1:])
                            lastdigs = _one_to_nnn(hundredphrase, reverse=True, nn=True)
                        else: # misspellings should not result in return value
                            return None
                    elif len(lastwords) == 5 and lastwords[2] == 'hundre': # 'tusen fire hundre og fem'
                        hundredphrase = ' '.join(lastwords[1:])
                        if nn == False:
                            lastdigs = _one_to_nnn(hundredphrase, reverse=True)
                        else:
                            lastdigs = _one_to_nnn(hundredphrase, reverse=True, nn=True)
                    else: # misspellings should not result in return value
                        return None
                    firstdigs = 0
                    firstphrase = ' '.join(firstwords)
                    if len(firstwords) == 0: # as in 'tusen og tretti'
                        firstdigs = 1000
                    elif len(firstwords) == 1 and firstwords[0] == 'ett' and nn == False:
                            firstdigs = 1000
                    elif len(firstwords) == 1 and firstwords[0] == 'eitt' and nn == True:
                            firstdigs = 1000
                    elif type(_one_to_nnn(firstphrase, reverse=True)) is int and nn == False:
                        firstdigs = _one_to_nnn(firstphrase, reverse=True)*1000
                    elif type(_one_to_nnn(firstphrase, reverse=True, nn=True)) is int and nn == True:
                        firstdigs = _one_to_nnn(firstphrase, reverse=True, nn=True)*1000
                    else:  # misspellings should not result in return value
                        return None
                    if type(firstdigs) is int and type(lastdigs) is int:
                        return firstdigs+lastdigs


def convert_nums(nr, reverse=False, nn=False):
    """Functions for converting numbers. Only works for numbers in range 0-999999 for now"""
    if reverse == False:
        if type(nr) is int:
            returnstring = ''
            if nr == 0:
                returnstring = 'null'
            elif nr < 1000000:
                if nn == False:
                    returnstring = _one_to_nnnnnn(nr)
                else:
                    returnstring = _one_to_nnnnnn(nr, nn=True)
            else:
                return None
            return returnstring
    else:
        if type(nr) is str:
            returnint = 0
            if nr == 'null':
                returnint = 0
            elif nn == False and type(_one_to_nnnnnn(nr, reverse = True)) is int:
                returnint = _one_to_nnnnnn(nr, reverse = True)
            elif nn == True and type(_one_to_nnnnnn(nr, reverse = True, nn=True)) is int:
                returnint = _one_to_nnnnnn(nr, reverse = True, nn=True)
            elif nn == False and type(_high_hundred(nr)) is int:
                returnint = _high_hundred(nr)
            elif nn == True and type(_high_hundred(nr, nn=True)) is int:
                returnint = _high_hundred(nr, nn=True)
            else:
                return None
            return returnint

if __name__ == "__main__":
    #testing    
    mydigit = 243564
    mynumstring = "hundre og atten tusen fire hundre og trettién"
    mydigit_nn = 34381
    mynumstring_nn = "tre hundre og førtiein"

    print("Digit conversion bm: %s\nString conversion bm: %s" % (convert_nums(mydigit), convert_nums(mynumstring, reverse=True)))
    print("Digit conversion nn: %s\nString conversion nn: %s" % (convert_nums(mydigit_nn, nn=True), convert_nums(mynumstring_nn, nn=True, reverse=True)))