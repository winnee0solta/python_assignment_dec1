# Author : Kishor shrestha
# Write a Python script to prove that (a+b)2 = a2+2ab+b2

def LHS(a, b):
    return (a + b) ** 2


def RHS(a, b):
    return a ** 2 + 2 * a * b + b ** 2


L = LHS(2, 3)
R = RHS(2, 3)

print("{} = {} , Hence proved".format(L, R))