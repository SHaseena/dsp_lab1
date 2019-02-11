import matplotlib.pyplot as plt
import numpy as np
w1=input("enter sampling frequency one:")
w2=input("enter sampling frequency two:")
p1=input("enter wave phase one:")
p2=input("enter wave phase two:")
a1=input("enter amplitude one:")
a2=input("enter amplitude two:")
sample=1000
t=np.arange(sample)
x1=a1*(np.cos((w1*t)+p1))
y1=a1*(np.cos((w2*t)+p1))
p1=a1*(np.cos((w1*t)+p2))
q1=a1*(np.cos((w2*t)+p2))
z1=x1+y1+p1+q1
plt.plot(t,z1)
plt.subplot(3,1,1)
x2=a1*(np.cos((w1*t)+p1))
y2=a2*(np.cos((w1*t)+p1))
p2=a1*(np.cos((w1*t)+p2))
q2=a2*(np.cos((w1*t)+p2))
z2=x2+y2+p2+q2
plt.plot(t,z2)
plt.subplot(3,1,2)
x3=a1*(np.cos((w1*t)+p1))
y3=a2*(np.cos((w1*t)+p1))
p3=a1*(np.cos((w2*t)+p1))
q3=a2*(np.cos((w2*t)+p1))
z3=x3+y3+p3+q3
plt.plot(t,z3)
plt.subplot(3,1,3)
plt.show()
