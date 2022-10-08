#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*x + 5

x1 = np.linspace(-1,1)
x2 = np.linspace(-6, 6)
x3 = np.linspace(0, 5)

print(x1)

plt.plot(x2, f(x2), 'y', linewidth = 5)
plt.plot(x3, f(x3), 'r', linewidth = 3)
plt.plot(x1, f(x1), 'b', linewidth = 1)
plt.title("Wykres funkcji f(x)=x^2+5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend([(-6,6), (0, 5), (-1, 1)])
plt.show()

plt.plot(x1, f(x1))
plt.title("Wykres funkcji f(x)=x^2+5 dla argumentów z zakresu (-1, 1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

plt.plot(x2, f(x2))
plt.title("Wykres funkcji f(x)=x^2+5 dla argumentów z zakresu (-6, 6)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

plt.plot(x3, f(x3))
plt.title("Wykres funkcji f(x)=x^2+5 dla argumentów z zakresu (-0, 5)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()





