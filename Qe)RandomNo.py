import numpy as np
import matplotlib.pyplot as plt
import time

"""
Things to do:
    -Figure out the theoretical timing ratio thing; ask people
    -formating the code and displaying the graphs nicely
    -fixing the seed to a singular value

"""

#%%
seed=np.random.seed()
v=np.random.uniform(0,1,10**5)

count, bins,ignored = plt.hist(v, 30,normed=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='red')
plt.show()
#%%

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

#%%
start = time.time()
x_new=[]
for i in p_new:
    y=2*np.arcsin(i)
    x_new.append(y)   

def pdf_3(x):
    return (2/np.pi)*np.cos(x/2)

Nreject_2=[]
counter=0
for i in range(len(x_new)):
    if pdf_2(x_new[i])>=pdf_3(np.random.uniform(0,np.pi)):
        Nreject_2.append(v_new[i])
        counter+=1
    if counter >= 10**5:
        break

plt.plot(ra,pdf_2(ra))
plt.hist(Nreject,30,normed=True)
plt.show()    
end = time.time()
print("time taken for the improved rejection method:",end - start)