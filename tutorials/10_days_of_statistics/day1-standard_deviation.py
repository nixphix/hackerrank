def mean(lst):
    return round(sum(lst)/(len(lst) if len(lst)!=0 else 1),1)

def sd(lst):
    m = mean(lst)
    sqd_dist = [(e-m)**2 for e in lst]
    return round((sum(sqd_dist)/len(lst))**(.5),1)

n = eval(input())
x = list(map(int,input().split(" ")))
print(sd(x))
