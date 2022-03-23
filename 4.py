def function (x):

    y = bin(x)
    cont=0

    for num in str(y):

        if num == '1':

            cont = cont + 1

    return 'conta_uns({}) --> {}\n{}\n'.format(x, cont, y)


x = int(input("Numero: "))
print(function(x))
