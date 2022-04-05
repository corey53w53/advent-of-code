from random import *
l=[53,73,173]
#1139 - 1368
counter=0
total_list=[]
total=[229,229,173,113,113]
while counter<1000:
    total.append(choice(l))
    if 1139<sum(total):
        if sum(total)<1233:
            total_list.append(sum(total))
        total=[229,229,173,113,113]
        counter+=1
total_list.sort()
print(sorted(list(set(total_list))))