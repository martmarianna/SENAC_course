produtos = {'nome':'mouse', 'preco': 49.90, 'estoque': 25}

consulta = produtos.get(input('Digite o nome de uma chave que você deseja consultar: '))

if consulta in produtos.keys():
    print (produtos.get(consulta))
else:
    print ('Essa informação não esta disponível')

nova_categoria = {'categoria': 'Informática'}
produtos.update(nova_categoria)

produtos['Informática'] = 59.90
print (produtos)

del produtos ['estoque']
print (produtos)