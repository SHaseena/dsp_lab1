import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter the value of m="))
l=int(input("enter the value of l="))
a=(7-1)/2
n=np.arange(0,a,0.1)
tri=(2*n)/(7-1)
rect=20*np.log(1)
X=[]
for n in range(0,a):
	h=0
	h=h+(0.5*(1-(np.cos((2*np.pi*n)/6))))
	X.append(h)
Y=[]
for n in range(0,a):
	ham=0
	ham=ham+(0.54-((1-0.54)*np.cos((2*np.pi*n)/6)))
	Y.append(ham)
Z=[]
for n in range(0,a):
	blat=0
	blat=blat+(0.4-((0.5*np.cos((2*np.pi*n)/6))-(0.08*np.cos((4*np.pi*n)/6))))
	Z.append(blat)
plt.subplot(151)
plt.plot(rect)
plt.subplot(152)
plt.plot(n,tri)
plt.subplot(153)
plt.plot(n,np.abs(X))
plt.subplot(154)
plt.plot(n,np.abs(Y))
plt.subplot(155)
plt.plot(n,np.abs(Z))
plt.show()
