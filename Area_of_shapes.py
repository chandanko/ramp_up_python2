import math

try:
    def area(*args):
        if len(args) == 1:
            print("Area of circle -> ", math.pi * (args[0] ** 2))
        elif len(args) == 2:
            print("Area of rectangle -> ", args[0] * args[1])
        elif len(args) == 3 and args[2] == "t":
            print("Area of Triangle -> ", 0.5 * args[0] * args[1])
        else:
            print("Do not give more than 3 args ")
except:
    print("Executed except block ")
# area(3, 6, "triangle")
try:
    Userin = input("enter the values separated by comma -> ")
    lst = Userin.split(",")

    if len(lst) == 3 and lst[-1] == "t":
        a, b, c = int(lst[0]), int(lst[1]), lst[2]
        area(a, b, c)
    elif len(lst) == 2:
        a, b = int(lst[0]), int(lst[1])
        area(a, b)
    elif len(lst) == 1:
        a = int(lst[0])
        area(a)
except:
    print("please check the valid length of values ")
