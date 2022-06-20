import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123456)

a1_true, a2_true = (np.random.random((2))-0.5)*2
b_true = 0.5

x1 = np.linspace(0,1,100)
y1 = a1_true*x1 + b_true + (np.random.random((len(x1)))-0.5)/5

x2 = np.linspace(-1,0,100)
y2 = a2_true*x2 + b_true + (np.random.random((len(x2)))-0.5)/5

A1 = np.vstack([x1, np.ones(len(x1))]).T
a1, b1 = np.linalg.lstsq(A1, y1, rcond=None)[0]

A2 = np.vstack([x2, np.ones(len(x2))]).T
a2, b2 = np.linalg.lstsq(A2, y2, rcond=None)[0]

angle = np.arctan((a1-a2)/(1+a1*a2))

print(f"a1_true={np.round(a1_true, 2)} - a1_inf={np.round(a1, 2)}")
print(f"a2_true={np.round(a2_true, 2)} - a2_inf={np.round(a2, 2)}")

plt.plot(x1,y1, "ob")
plt.plot(x2,y2, "ob")

plt.plot(x1, a1*x1+b1, "-r")
plt.plot(x2, a2*x2+b2, "-r", label=f"Angle={np.round(angle*180/np.pi, 2)}°")

plt.xlim([-1,1])
plt.ylim([0,1])
plt.gca().set_aspect("equal")

plt.legend()

plt.show()