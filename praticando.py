print('Praticando o uso de Listas e Loops\n1 - Exericicio de mostrar todas as listas\n2 - Exercicio de somar a lista numeros\n3 - Exercicio de Ordem descrescente da lista numeros\n4 - Tabuada do Número escolhido\n5 - Calculo de média')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Pedro', 'Fernando', 'Roberto', 'Maria']
anos = [2007, 2026]
lista = []
lista_calculo = [60, 40]
opcao = int(input('Digite uma Opção: '))
def percorrer_listas():
    print('Lista Números')
    for numero in numeros:
        print(f'"{numero}"')
    print('Lista de Nomes:')
    for nome in nomes:
        print(f'Nome: {nome}')
    print('Lista de Anos')
    for ano in anos:
        print(f'Anos: {ano}')

def soma_impares():
    for numero in numeros:
        if numero % 2 == 0:
            lista.append(numero)
            somando = sum(lista)
        else:
            pass
    print(lista)
    print(f'Soma: {somando}')
def ordem_descrescente():
    numeros.sort(reverse=True)
    print(numeros)
def tabuada():
    ver_tabuada = int(input('Insira o valor para visualizar a Tabuada: '))
    for i in range(1, 11):
        print(f'{ver_tabuada} x {i} = {ver_tabuada * i}')

def tentativa():
    print(f"Vamos somar os números: {lista_calculo}")
    try:
        somar = sum(lista_calculo)
        print(somar)
    except:
        print('Erro ao somar') 

def media():
    print(f'Vamos calcular a Média da lista: {numeros}')
    quantidade = len(numeros)
    somando_todos = sum(numeros)
    calcula_media = somando_todos / quantidade
    print(calcula_media)
match opcao:
    case 1: 
        percorrer_listas()
    case 2:
        soma_impares()
    case 3:
        ordem_descrescente()
    case 4:
        tabuada()
    case 5:
        tentativa()
    case 6:
        media()
    case _:
        print("Opção Invalida")