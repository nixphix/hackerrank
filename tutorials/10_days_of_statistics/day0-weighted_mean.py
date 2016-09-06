#!/usr/bin/python
n = eval(input())
v = list(map(int,input().split(" ")))
w = list(map(int,input().split(" ")))
wt_avg = round(sum([a*b for a,b in zip(v,w)])/sum(w),1)
print(wt_avg)
