print ('Bem-vindo ao sistema de votação!')

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

lista_goku = []
lista_naruto = []
lista_luffy = []

if idade >= 14:
    print ('Você esta apto a votar!')

    candidato = input ('Escolha seu candidato:\n 1 - Goku\n2-Naruto\n3-Luffy')
    
    voto_goku = 0
    voto_naruto = 0
    voto_luffy = 0

    if candidato == 1:
        print ('Você escolheu GOKU!')
        voto_goku +=1
    elif candidato == 2:
        print ('Você escolheu NARUTO!')
        voto_naruto +=1
    elif candidato == 3:
        print ('Você escolheu GOKU!')
        voto_luffy +=1

else:
    print ('Você não pode votar. :/ ')

