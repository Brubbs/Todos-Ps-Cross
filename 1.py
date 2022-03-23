import math
math.pi

def function(num):

    y = num * (180/math.pi)
    return ('readianos_graus({}) --> {:.1f}'.format(num, y))

z=1
while z==1:

    x = int(input("Digite um ângulo em radianos: "))
    print(function(x))
