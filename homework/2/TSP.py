from math import sqrt
from functools import cache # 讓重複引用 Function 時更快
from random import sample

citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

#path = [i for i in range(len(citys))]
l = len(citys)
path=tuple([(i+1)%l for i in range(l)])
print(path)

# 計算兩點距離
@cache
def distance(p1:tuple,p2:tuple)->float:
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

# 計算此路徑陣列的總距離
@cache
def pathLength(path:tuple)->float:
    dist = 0
    for i in range(len(path)):
        dist += distance(citys[i], citys[path[i]])
    return dist

# 爬山演算法：找出可能最佳解
def hillClimbing(path:list[int])->list[int]:
    fail=0
    while fail<100000:
        temp=list(path)

        swap_x,swap_y=sample(range(len(path)),2)
        while temp[swap_x]==swap_y or temp[swap_y]==swap_x:
            swap_x,swap_y=sample(range(len(path)),2)
        temp[swap_x],temp[swap_y]=temp[swap_y],temp[swap_x]

        temp=tuple(temp)
        if pathLength(temp)<pathLength(path):
            path=temp
            fail=0
            print(path,pathLength(path))
        else:
            fail+=1
    return path

ans=hillClimbing(path)
print(ans,pathLength(ans))