# Number conversion

## General info
This repo contains scripts that converts numbers written as digits to numbers written with
Norwegian words, and conversely, from numbers written as Norwegian words to digits. The scripts
support cardinal and ordinal numbers from 0-999999, and handles both written standards of Norwegian.

This is work in progress. I plan to add support for dates, years etc. and refactor the code
so that it becomes more readable.

- cardinal_numbers.py
    Digit to string, Bokmål:
        convert_nums(21) -> "tjueén"
    Digit to string, Nynorsk:
        convert_nums(21, nn=True) -> "tjueein"
    String to digits, Bokmål:
        convert_nums("tjueén", reverse=True) -> 21
    String to digits, Nynorsk:
        convert_nums("tjueein", nn=True, reverse=True) -> 21
    
- ordinal_numers.py
    Digit to string, Bokmål:
        convert_ords(16) -> "sekstende"
    Digit to string, Nynorsk:
        convert_ords(16, nn=True) -> "sekstande"
    String to digits, Bokmål:
        convert_ords("sekstende", reverse=True) -> 16
    String to digits, Nynorsk:
        convert_ords("sekstande", nn=True, reverse=True) -> 16
    
    Examples are added at the end of each scripts

- regression_numbers.py
    tests all the functionality in cardinal_numbers.py (conversion both ways for 
    Bokmål and Nynorsk). It prints out lists of numbers between 0 and 999999 for which
    convert_nums() maps to None (i.e. fails), and prints out the lists. All lists should
    be empty. If some of the lists are non-empty after modifying the script, the content
    of the lists might indicate where the problem is.

## Author
These scripts are made by Per Erik Solberg at the National Library of Norway as part of
Språkbankens parliamentary proceedings transcription project 

