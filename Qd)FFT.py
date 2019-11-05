import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

T_max=7
T_min=-7
N=0.1
t=np.arange(T_min,T_max,step=N)
#if np.log2((T_max-T_min)/N).is_integer()==False:
#    b=(T_max-T_min)/N
#    a= 2**(np.log2((T_max-T_min)/N)//1 +1)-b
#    print(a,b)
#    for i in range(int(a)):
#        np.append(t,0)

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
#    if i>=0 and i<=1:
#        g.append(1)
#    else:
#        g.append(0)


w_max=1/(2*N)


    
H=fft.fft(h)
H_inv=fft.ifft(H,norm="ortho")
G=fft.fft(g)
G_inv=fft.ifft(G,norm="ortho")
conv=N*H*G# figure out why the N thin fixes everything!!!!

H_theo=2*np.abs(H/len(h))
G_theo=2*np.abs(G/len(h))
cov_theo=2*np.abs(conv/len(h))

w=fft.fftfreq(len(H))
w_pos=w>0

w_max_boader=[100,-50]

conv_inv=fft.ifft(conv)
plt.figure(1,figsize=(100,100))
plt.subplot(1,3,1)
plt.plot(t,h,'.-',label="h(t)")
plt.plot(t,g,'.-',label="g(t)")
plt.plot(t,conv_inv,'.-',label="g*h(t)")
plt.legend()
plt.grid()

plt.subplot(1,3,2)
#plt.plot([w_max,w_max],w_max_boader)
#plt.plot([-w_max,-w_max],w_max_boader)
plt.plot(w,G,'.-',label="G(w)")
plt.plot(w,H,'.-',label="H(w)")
plt.plot(w,conv,'.-',label="G(w).H(w)")
plt.legend()
plt.grid()

plt.subplot(1,3,3)
plt.plot(w[w_pos],H_theo[w_pos],'.-',label="H(w)")
plt.plot(w[w_pos],G_theo[w_pos],'.-',label="G(w)")
plt.plot(w[w_pos],cov_theo[w_pos],'.-',label="G(w).H(w)")
plt.legend()
plt.grid()



#plt.plot(t,G_inv,'+')

plt.show()
    

