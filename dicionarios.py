pessoa = {'nome': 'Pedro', 'idade': '20', 'cidade': 'São Paulo'}
pessoa['idade'] = 22

print(pessoa)

pessoa['profissao'] = 'Programador'
print(pessoa)
del pessoa['cidade']
print(pessoa)
 

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

dicionario = {'materia': 'artes', 'inscricoes': '32'}

pessoa_02 = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa_02:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur consectetur ultrices dignissim. Curabitur a porta metus. Cras non elementum sem.'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)