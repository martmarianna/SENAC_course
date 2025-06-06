usuarios_filmes = {'Cassio': ['Constantine', 'Vingadores'], 'Maria': [], 'João': ['Titanic', 'Avatar'] }



while True:
    try:
        opcao = int (input ('O que deseja fazer?\n1 - adicionar filme\n2 - remover filme\n3 - ver filmes de um usuário\n4 - ver todos os usuários\n0 - sair\n'))
    except:
        print ('Digite um valor válido!')
    match opcao:
        case 1:
            usuario = input ('Quem assistiu o filme? ').title()
            if usuario in usuarios_filmes:
                filme = input('Qual filme você quer adicionar?').title()
                usuarios_filmes[usuario].append(filme)
                print (f'Filme {filme} adicionado ao cadastro de {usuario} com sucesso!')
            else:
                print ('O usuário não esta cadastrado!')
                
        case 2:
            usuario = input ('Quem assistiu o filme? ').title()
            filme = input('Qual filme você quer remover? ').title()
            usuarios_filmes[usuario].remove(filme)
            print (f'Filme apagado do cadastro de {usuario} com sucesso!\nFilmes atuais: {usuarios_filmes[usuario]}')

        case 3:
            usuario = input ('A lista de filmes de quem você quer olhar? ').title()
            print(usuarios_filmes.get(usuario))

        case 4:
            print (usuarios_filmes)
            
        case 0:
            print ('Saindo...')
            break