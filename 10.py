import random
def function(n):

    cont = 0
    
    for i in range (n):
    
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if ((x*x + y*y)<1):
        
            cont = cont + 1

    pi = 4*(cont/n)

    return '{:.5f}'.format(pi)

n = 200000
print(function(n))
