import matplotlib.pyplot as plt
import numpy as np

#Constant variable
w=2
b=3

# independent variable x
x=np.arange(-10,10,0.1)

# for y=wx+b
y1=w * x + b

# for y=x^2
y2= x **2

# for y = 1/ (1 + e^(-x))
y3= 1/(1+np.exp(-x))

#for y = (e^x - e^(-x)) / (e^x - e^(-x))
y4=((np.exp(x)-np.exp(-x))/(np.exp(x)-np.exp(-x)))



#for y = g(f(x)) where u = f(x) = wx + b and y = g(u) = 1/ (1 + e^(-u))
y5= 1/(1+np.exp(-y1))

#for y = g(f(x)) where f(x) = wx + b, u = f(x), and g(u) = (e^u - e^(-u)) / (e^u - e^(-u))
y6=((np.exp(y1)-np.exp(-y1))/(np.exp(y1)-np.exp(-y1)))


# for y = g3(f3(v)) where f3(v) = w3y1 + w4y2 + b, w = f3(v), and g3(w) = 1/ (1 + e^(-w))

#for g1(f1(x)) where f1(x) = w1x + b1, u1 = f1(x), and g1(u1) = 1/ (1 + e^(-u1))
w1=5
b1=7
x2= w1*x + b1
y7=1/(1+np.exp(-x2))  

#for y2 = g2(f2(x)) where f2(x) = w2x + b2, u2 = f2(x), and g2(u2) = 1/ (1 + e^(-u2))
w2=10
b2=15
x1=w2*x + b2
y8=1/(1+np.exp(-x1))

w3=10
w4=12
b=7
y9=w3*y7+w4*y8+b
y10=1/(1+np.exp(-y9))


plt.figure(figsize=(10, 10))
plt.subplot(4,2,1)
plt.plot(x,y1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = wx + b')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.subplot(4,2,2)
plt.plot(x,y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.subplot(4,2,3)
plt.plot(x,y3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 1/ (1 + e^(-x))')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.subplot(4,2,4)
plt.plot(x,y4)
plt.xlabel('x')
plt.ylabel('y')
plt.title(' y = (e^x - e^(-x)) / (e^x - e^(-x))')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.subplot(4,2,5)
plt.plot(x,y5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=g(f(x)) where u=f(x)=wx+b and y=g(u)= 1/(1 + e^(-u)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.subplot(4,2,6)
plt.plot(x,y6)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=g(f(x)) where f(x)=wx + b,u =f(x),andg(u)=(e^u - e^(-u))/(e^u - e^(-u))')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)


plt.subplot(4,2,7)
plt.plot(x,y10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y =g3(f3(v)) where f3(v) = w3y1 + w4y2 + b,w = f3(v), and g3(w) = 1/ (1 + e^(-w))')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)



plt.tight_layout()
plt.savefig('Assignment 1', dpi=300)
plt.show()

