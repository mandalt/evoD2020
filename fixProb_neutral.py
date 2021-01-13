#fixation probability for neutral evolution
#Q2_1
import random
import numpy as np
import math
import matplotlib.pyplot as plt
N=100.0
x0=50
x1=N-x0
r=.99
freq0=[]
freq1=[]
cnt0=0
cnt1=0
n=0
prob0=r*x0/(r*x0+x1)
prob0_d=x0/100.
#print (prob0+prob1)    
while x0!=100 and x1!=100:
    rand1=random.random()
    rand2=random.random()
    n=n+1
    if rand1<prob0:
        x0=x0+1
    else:
        x1=x1+1
    if rand2<prob0_d:
        x0=x0-1
    else:
        x1=x1-1
    #print(x0+x1)
    y0=x0/100.
    y1=x1/100.
    freq0.append(y0)
    freq1.append(y1)
    prob0=r*x0/(r*x0+x1)
    prob1=1*x1/(x1+x0*r)
    prob0_d=x0/100.
    #print(prob0+prob1)
print(n)
t=np.arange(n)
plt.plot(t,freq0,freq1)
plt.ylabel('frequency')
plt.xlabel('time(generations)')
plt.legend(['species_0','species_1'])
plt.suptitle('Reproduction is fitness dependent')
plt.show()


# In[32]:


#Q2_2
import random
import numpy as np
import math
import matplotlib.pyplot as plt
N=100.0
Nt=1000
x0=50.
x1=N-x0
r=.99
freq0=[]
freq1=[]
cnt0=0
cnt1=0
n=0
prob0=r*x0/(r*x0+x1)
prob1=1*x1/(x1+x0*r)
prob0_d=x0/100.
#prob1_d=x1/100.
print (prob0+prob1)    
for i in range(Nt):
    x0=50.
    x1=N-x0
    prob0=r*x0/(r*x0+x1)
    prob1=1*x1/(x1+x0*r)
    prob0_d=x0/100.
    while True:
        rand1=random.random()
        rand2=random.random()
        n=n+1
        if rand1<prob0:
            x0=x0+1
        else:
            x1=x1+1
        if rand2<prob0_d:
            x0=x0-1
        else:
            x1=x1-1
        y0=x0/100.
        y1=x1/100.
        freq0.append(y0)
        freq1.append(y1)
        prob0=r*x0/(r*x0+x1)
        prob1=1*x1/(x1+x0*r)
        prob0_d=x0/100.
        if x0==100:
            cnt0=cnt0+1
            break
        if x1==100:
            cnt1=cnt1+1
            break
fix_prob0=cnt0/Nt
fix_prob1=cnt1/Nt
print(fix_prob0,fix_prob1)



