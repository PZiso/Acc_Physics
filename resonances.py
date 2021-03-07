import numpy as np
import matplotlib.pylab as plt

qx = np.linspace(0,1,5)
ks = np.linspace(-10,10,21,dtype = int)
ls = np.linspace(-10,10,21,dtype = int)
order = 5

color = 'teal'
for k in ks:
    for l in ls:
        if abs(k) + abs(l) <= order:
#             print('in')
            if k!=0:
                if l != 0:
                    a = k/l
                    m = - 10
                    while m <= min(abs(l) + abs(k)*qx): 
#                         print('in')
                        b = m/l
                        qy = a*qx + b
                        
                        plt.plot(qx,qy,color)
                        m+=1
                elif l == 0:
                    m=0
                    while m <= k:
                        x0 = m/k
                        plt.vlines(x0,0,1,color)
                        m+=1
            elif k == 0:
                if l!=0:
                    m = 0
                    while m <= l: 
                        y0 = m/l
                        plt.hlines(y0,0,1,color)
                        m+=1
                else:
                    continue
        else:
            continue
        
plt.ylim(0,1)   
plt.xlim(0,1)

qx0,qy0 = 0.38,0.28

plt.plot(qx0,qy0,'o',color = 'darkorange',markeredgecolor = 'k',markersize = 9,label = 'Working point')
plt.xlabel('Q$_x$')
plt.ylabel('Q$_y$')
plt.show()