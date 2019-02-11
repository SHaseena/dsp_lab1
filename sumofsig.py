import matplotlib.pyplot as plt
import numpy as np
w1=input("enter sampling frequency one:")
w2=input("enter sampling frequency two:")
p1=input("enter wave phase one:")
p2=input("enter wave phase two:")
a1=input("enter amplitude one:")
a2=input("enter amplitude two:")
sample=500
t=np.arange(sample)
l1=a1*(np.cos((w1*t)+p1))
m1=a2*(np.cos((w1*t)+p1))
n1=l1+mc1
plt.plot(t,n1)
plt.subplot(3,1,1)
l2=a1*(np.cos((w1*t)+p1))
m2=a1*(np.cos((w2*t)+p1))
n2=l2+m2
plt.plot(t,n2)
plt.subplot(3,1,2)
l3=a1*(np.cos((w1*t)+p1))
m3=a1*(np.cos((w1*t)+p2))
n3=l3+m3
plt.plot(t,n3)
plt.subplot(3,1,3)
plt.show()
