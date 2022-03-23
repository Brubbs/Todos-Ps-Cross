import math
def function (x, y, x1, y1):

    d = math.sqrt((x-x1)*(x-x1) + (y-y1)*(y-y1))

    return 'distancia (({},{}), ({}, {})) --> {:.2f}'.format(x,y,x1,y1,d)

x = int(input('x: '))
y = int(input('y: '))
x1 = int(input('x1: '))
y1 = int(input('y1: '))

print(function(x,y,x1,y1))
