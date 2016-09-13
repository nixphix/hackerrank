#!/usr/bin/python

def mean(lst):
    return round(sum(lst)/(len(lst) if len(lst)!=0 else 0),1)

def median(lst):
    lst.sort()
    lst_len=len(lst)
    return round(lst[(lst_len)//2],1) if lst_len%2 != 0 else mean(lst[(lst_len-1)//2:][:2])

def odd_even(lst):
    lst.sort()
    n = len(lst)//2
    return (lst[:n],lst[-n:])

n = input()
x = list(map(int,input().split(" ")))
splitx = odd_even(x)

print("{0:g}".format(median(splitx[0])))
print("{0:g}".format(median(x)))
print("{0:g}".format(median(splitx[1])))
