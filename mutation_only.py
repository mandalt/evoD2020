
# # Evolution with mutation without selection
# ##x and y are frequencies of 2 species. Mutation rate from x>y:u1, y>x:u2
# ##a0 denotes the frequencies of species '0' and a1 denotes that of species '1' over time=t


import random
import numpy as np
import matplotlib.pyplot as plt

u1=.003
u2=.001
pop_size=10000
t=1500
N=np.random.randint(0,1+1,pop_size)
a0=[]
a1=[]
for j in range(t):
    for i in range(len(N)):
        x=N[i]
        if x==0:
            r=random.random()
            if r<u1:
                x=1
            else:
                x=0
        else:
            r=random.random()
            if r<u2:
                x=0
            else:
                x=1
        N[i]=x
    #print(N,r)
    N=N.astype(int)
    b2=np.bincount(N)
    b2=b2.astype(float)
    a0.append(b2[0]/len(N))
    a1.append(b2[1]/len(N))
    b=np.arange(1,t+1,1)

plt.plot(b,a0,a1)
plt.ylabel('frequency')
plt.xlabel('time(generations)')
plt.legend(['species_0','species_1'])
plt.suptitle('evolution of 2 species under mutation and no selection')
plt.title('N=10000,t=1500,u1=.003,u2=.001')

plt.show()






