import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

T_max=8
T_min=-8
N=0.1
t=np.arange(T_min,T_max,step=N)

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


w_max=1/(2*(T_max-T_min)/N)


    
H=fft.fft(h,norm="ortho")
H_inv=fft.ifft(H,norm="ortho")
G=fft.fft(g,norm="ortho")
G_inv=fft.ifft(G,norm="ortho")
conv=H*G

w=fft.fftfreq(len(H))

w_max_boader=[100,-50]

conv_inv=fft.fft(conv,norm="ortho")
plt.figure(1,figsize=(100,100))
plt.subplot(1,2,1)
plt.plot(t,h,label="h(t)")
plt.plot(t,g,label="g(t)")
plt.plot(t,conv_inv,'.',label="g*h(t)")
plt.legend()

plt.subplot(1,2,2)
#plt.plot([w_max,w_max],w_max_boader)
#plt.plot([-w_max,-w_max],w_max_boader)
plt.plot(w,G,label="G(w)")
plt.plot(w,H,label="H(w)")
plt.plot(w,conv,label="G(w).H(w)")
plt.legend()



#plt.plot(t,G_inv,'+')

plt.show()
    

