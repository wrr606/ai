import numpy as np
from numpy.linalg import norm
from micrograd.engine import Value

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, h=0.01, max_loops=100000, dump_period=1000):
    p = p0.copy()
    for i in range(max_loops):
        fp = f(p)
        gp,t=[],[]
        for j in range(len(p)):
            t.append(Value(p[j]))
        f(t).backward()
        for j in t:
            gp.append(j.grad)
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        if i%dump_period == 0: 
            print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
        if glen < 0.00001: # 如果步伐已經很小了，那麼就停止吧！
            break
        gh = np.multiply(gp, -1*h) # gh = 逆梯度方向的一小步
        p +=  gh # 向 gh 方向走一小步
    print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
    return p # 傳回最低點！

def f(p):
    [x, y, z] = p
    return (x-1)**2+(y-2)**2+(z-3)**2
    # return (x-2)**2+3*(y-0.5)**2+(z-2.5)**2
    # return x*x + 3*y*y + z*z - 4*x - 3*y - 5*z + 8

p = [0.0, 0.0, 0.0]
gradientDescendent(f, p)