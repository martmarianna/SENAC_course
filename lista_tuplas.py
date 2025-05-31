nomes = []
n = 0

while (n <= 4):
    try:
        nome = input ('Digite um nome: ')
        nomes.append(nome)
        n += 1
    except:
        print ('Digite um nome, não números.')
print (nomes)
