#!/usr/bin/python

def median(lst):
    lst.sort()
    lst_len=len(lst)
    return round(lst[(lst_len+1)//2],1) if lst_len%2 != 0 else mean(lst[(lst_len-1)//2:][:2])

def odd_even(lst):
