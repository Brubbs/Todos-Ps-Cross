def function(x):

    if x%3 == 0 and x%5 != 0:

        return 'Cross'
    
    if x%5 == 0 and x%3 != 0:

        return 'Bots'

    if x%3 == 0 and x%5 == 0:

        return 'CrossBots'
    
    if x%3 != 0 and x%5 != 0:

        return x
z=1
while z==1:
    
    num = int(input("Numero: "))
    print(function(num))
