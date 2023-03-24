#!/usr/bin/python3

a, b, c = 2, 4, 4
delta = b ** 2 - 4 * a * c
x1, x2 = (-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a)

print(x1)
print(x2)