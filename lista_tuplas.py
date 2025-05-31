nomes = []
n = 0

while (n < 5):
    try:
        nome = input ('Digite um nome: ')
        nomes.append(nome)
        n += 1
        
    except:
        print ('Digite um nome, não números.')
        break

print (nomes)

try:
    remova = nomes.remove(input ('Escolha um nome para ser removido da lista.'))

except:
    print ('Você não escreveu um nome que esteja na lista')

print (nomes)
