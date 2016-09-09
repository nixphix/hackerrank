#!/usr/bin/python

def median(lst):
    lst.sort()
    lst_len=len(lst)
    return round(lst[(lst_len+1)//2],1) if lst_len%2 != 0 else mean(lst[(lst_len-1)//2:][:2])

def odd_even(lst):
    n = len(lst)//2
    return tuple(lst[:n],lst[-n:])
    
n = input()
x = map(int,input().split(" "))
splitx = odd_even(x)

print(median(splitx[0]))
print(median(x))
print(median(splitx[1]))
