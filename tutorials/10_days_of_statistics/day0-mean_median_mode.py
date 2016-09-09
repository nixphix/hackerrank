#!/usr/bin/python
import collections

def mean(lst):
    return round(sum(lst)/(len(lst) if len(lst)!=0 else 1),1)

def median(lst):
    lst.sort()
    lst_len=len(lst)
    return round(lst[(lst_len)//2],1) if lst_len%2 != 0 else mean(lst[(lst_len-1)//2:][:2])
  
def mode(lst):
    lst.sort()
    elemnt = collections.Counter(lst).most_common()
    first_elemnt = elemnt[0]
    return sorted([e[0] for e in elemnt if e[1]==first_elemnt[1]])[0]
  
n = eval(input())
x = list(map(int,input().split(" ")))
print(mean(x))
print(median(x))
print(mode(x))
