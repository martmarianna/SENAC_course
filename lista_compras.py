itens = []
precos = []

#para lista de itens
while True:
    try:
        n = 0
        while (n<3):
            produtos = input(f'Digite {n+1}º produto: ')

            itens.append(produtos)
            n += 1

    except: 
        print ('Digite o nome de produtos válidos.')
    break

#para lista de valores
while True:
    try:
        for c in range (0,3):
            preco = float(input('Digite o respectivo valor de cada produto: '))

            precos.append(preco)
            
    except: #conferir se o tipo de dado é numeral
        print ('Digite um valor válido para os preços.')
    break

n = 0
while n < len(itens):
    print (f'O produto {itens[n]} custa R$ {precos[n]:.2f}.')
    n += 1

