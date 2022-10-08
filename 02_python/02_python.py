import math
from tkinter import Y

age = 28
height = 1.62
store = 1+3j

base_triangle = int(input('Base: '))
heigth_triangle = int(input('Heigth: '))
area = 0.5 * base_triangle * heigth_triangle

print('The area of the triangle is', area)

side_triangle_a = int(input('Enter side a: '))
side_triangle_b = int(input('Enter side b: '))
side_triangle_c = int(input('Enter side c: '))

perimeter = side_triangle_a + side_triangle_b + side_triangle_c

print('The perimetrer of the triangle is ', perimeter)

length = int(input('length: '))
width = int(input('width: '))

area = length * width
perimeter = 2 * (length + width)

print('Perimeter is: ', perimeter)
print('Area is: ', area)

pi = 3.14

radius = int(input('radius: '))
area = pi * radius * radius

print('Area of the circle is: ', area)

circunference = 2 * pi * radius

print('Circunference is: ', circunference)

# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = int()
m = int(input())

y = (m * x - 2)
slope = m

print(slope)

# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1, y1 = int(input('x1: ')), int(input('y1: '))
x2, y2 = int(input('x2: ')), int(input('y2: '))

y = y2 - y1
x = x2 - x1

slope = y / x

print(slope)


