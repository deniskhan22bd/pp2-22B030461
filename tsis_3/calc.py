import math
def Trapezoidalarea(nums: list):
    area = 0
    for i in range(len(y_list)):
        if i == 0:
            area += y_list[i]
        elif i == len(y_list) - 1:
            area += y_list[i]
        else:
            area += y_list[i] * 2

    print(delta_x / 2 * area)

def Simpsonarea(nums: list):
    area = 0
    for i in range(len(y_list)):
        if i == 0:
            area += y_list[i]
        elif i == len(y_list) - 1:
            area += y_list[i]
        elif i % 2 == 1:
            area += y_list[i] * 4
        else:
            area += y_list[i] * 2
    print(delta_x / 3 * area)



y = input("your func:")
a = int(input("a = "))
b = int(input("b = "))
n = int(input("n = "))
delta_x = (b - a) / n
y_list = list()

for i in range(n + 1):
    y_list.append(5 * (a ** 4))
    a += delta_x

#print(y_list)

Trapezoidalarea(y_list)
Simpsonarea(y_list)

