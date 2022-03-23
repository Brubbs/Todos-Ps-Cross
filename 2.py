def function(hr):
    list =[]*5

    m = hr/720
    list.append(int(m))

    s = hr/168
    list.append(int(s))

    mi = hr*60
    list.append(int(mi))

    seg = hr*3600
    list.append(int(seg))

    mil = hr*3600000
    list.append(int(mil))
    
    return 'Converter({})--> {}'.format(hr, list)
z=1
while z==1:
    horas = int(input("Digite um número de horas: "))
    print(function(horas))
