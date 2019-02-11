import matplotlib.pyplot as plt
import numpy as np
w1=input("enter sampling frequency one:")
p1=input("enter wave phase one:")
p2=input("enter wave phase two:")
a1=input("enter amplitude one:")
sample=500
t=np.arange(sample)
x3=a1*(np.cos((w1*t)+p1))
y3=a1*(np.cos((w1*t)+p2))
z3=x3+y3
plt.plot(t,z3)
plt.show()
