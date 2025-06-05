usuarios_filmes = {'Cassio': ['Constantine', 'Vingadores'], 'Maria': [], 'João': ['Titanic', 'Avatar'] }

usuario = input ('Quem assistiu o filme? ')
filme = input('Qual filme você quer adicionar?')
usuarios_filmes[usuario] = usuarios_filmes.append(filme)
#print (f'Filme {filme} adicionado ao cadastro de {usuario} com sucesso!')
print (usuarios_filmes)

# usuario = input ('Quem assistiu o filme? ').title()
# filme = input('Qual filme você quer remover? ').title()
# usuarios_filmes[usuario].remove(filme)
# print (f'Filme apagado do cadastro de {usuario} com sucesso!\nFilmes atuais: {usuarios_filmes[usuario]}')

# usuario = input ('A lista de filmes de quem você quer olhar? ').title()
# print(usuarios_filmes.get(usuario))

