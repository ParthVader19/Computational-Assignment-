import numpy as np
import matplotlib.pyplot as plt

#%%
seed=np.random.seed()
v=np.random.uniform(0,1,10**5)

count, bins,ignored = plt.hist(v, 30,normed=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='red')
plt.show()
#%%
v_new=np.random.uniform(0,1,10**5)
x=[]
for i in v:
    y=2*np.arcsin(i)
    x.append(y)   

ra=np.arange(0,np.pi,0.1)

def pdf(x=ra):
    return np.cos(x/2)/2

    
plt.hist(x,30,normed=True)
plt.plot(ra,pdf(ra))
plt.show()

#%%
v_new=np.random.uniform(0,np.pi,10**6)
p_new=np.random.uniform(0,1,10**6)

def pdf_2(x):
    return (2/np.pi)*np.cos(x/2)**2
Nreject=[]
counter=0
for i in range(len(v_new)):
    if pdf_2(v_new[i])>=p_new[i]:
        Nreject.append(v_new[i])
        counter+=1
    if counter >= 10**5:
        break

 
plt.plot(ra,pdf_2(ra))
plt.hist(Nreject,30,normed=True)
plt.show()
    