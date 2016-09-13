#!/usr/bin/python

def mean(lst):
    return round((sum(lst)/len(lst) if len(lst) != 0 else 0),1)

def median(lst):
    lst.sort()
    lst_len=len(lst)
    return round(lst[(lst_len)//2],1) if lst_len%2 != 0 else mean(lst[(lst_len-1)//2:][:2])

def odd_even(lst):
    lst.sort()
    n = len(lst)//2
    return (lst[:n],lst[-n:])

def interquartile_range(lst):
    lst_1,lst_2 = odd_even(lst)
    q1 = median(lst_1)
    q3 = median(lst_2)
    return round(float(q3-q1),1)

n = eval(input())
x = list(map(int,input().split(" ")))
f = list(map(int,input().split(" ")))
s = []

for i in range(n):
    s.extend([x[i]]*f[i])

print(interquartile_range(s))
