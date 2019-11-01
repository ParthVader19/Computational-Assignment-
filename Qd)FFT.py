import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

N= 100
t=np.linspace(-8,8,N,endpoint=False)

h=[]
for i in t:
    if i>=3 and i<=5:
        h.append(4)
    else:
        h.append(0)

g=[]   
for i in t:
    a=np.exp(-i**2 /2)/np.sqrt(2*np.pi)
    g.append(a)


    
H=fft.fft(h)
G=fft.fft(g)
conv=H*G

conv_inv=fft.ifft(conv)
plt.plot(t,h,label="h")
plt.plot(t,g,label="g")
plt.plot(t,conv_inv)
plt.legend()

plt.show()
    

