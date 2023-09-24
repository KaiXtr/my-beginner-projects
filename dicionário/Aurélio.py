lista=['Owl', 'Coffee', 'Linux', 'Geek']
ask=""
i=0

while (ask!="\\ext"):
    ask=str(input('>'));

    if ask== "\\add":
        print("Insira a palavra a ser adicionada")
        ask=str(input(">"))
        lista.append(ask);

    elif ask=="\\shw":
        while i <len(lista):
            print(lista[i])
            i+=1

    else:
        if ask in lista:
            print(ask + ' está no dicionário!');

        else:
            print(ask + ' não está no dicionário...');