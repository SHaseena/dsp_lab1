import matplotlib.pyplot as plt
import numpy as np
Fs=input("enter sampling frequency")
f1=input("enter first frequency")
f2=input("enter second frequency")
sample=1000
k=np.arange(sample)
l=np.cos(2*np.pi*f1*k/Fs)
m=np.cos(2*np.pi*f2*k/Fs)
n=l+m
plt.subplot(3,1,1)
plt.plot(k,l)
plt.subplot(3,1,2)
plt.plot(k,m)
plt.subplot(3,1,3)
plt.plot(k,n)
plt.show()

