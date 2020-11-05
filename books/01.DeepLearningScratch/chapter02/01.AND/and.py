# coding: utf-8
import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7


print("{} np array Type".format(w*x))
print("{} np array sum ".format(np.sum(w*x)))
print("{} np AND ".format(np.sum(x*w) + b))
