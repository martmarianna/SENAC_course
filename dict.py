# produtos = {'mouse': 59.90, 'teclado': 89.90, 'tela': 190.00}
# print (produtos)

# produtos.pop('mousepad', "Não existe esse produto no estoque")
# print (produtos)

########################################################
estoque = {'nome':'mouse', 'preco': 49.90, 'estoque': 25}

cadastro = input('Deseja adicionar um produto ao estoque? ')

estoque.update(cadastro)

print (estoque)

consulta = estoque.get(input('Qual produto você deseja consultar? '))

print(consulta)

for k, v in estoque.items():
    print (f'O produto {k} custa R$ {v}.' )

####################################
# estoque = {'nome':'mouse', 'preco': 49.90, 'estoque': 25}

# consulta = estoque.get(input('Digite o nome de uma chave que você deseja consultar: '))
# if consulta in estoque:
#     print ('O produto existe no estoque.')
# else:
#     print ('Essa informação não esta disponível')

# nova_categoria = {input('Qual categoria deseja adicionar? ')}
# estoque.update(nova_categoria) #adicionar chave e valor

# print (estoque)

# estoque['Informática'] = 59.90

# print (estoque)

