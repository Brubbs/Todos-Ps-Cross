def function(item,n):


    list = [item for i in range (n)]

    return 'repeti("{}", {}) --> {}'.format(item,n,list)   

item = str(input("Digite uma palavra: "))
n = int(input("Digite o número de repetições: "))
print(function(item,n))


