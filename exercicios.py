def pares_impares():
    print('Verificação de Número par ou impar')
    numero_escolhido = int(input('Insira o numero: '))
    if numero_escolhido % 2 == 0:
        print('Par')
    else:
        print('Impar')

def idades():
    print('Qual a idade do usuário:')
    coletar_idade = int(input('Insira a idade: '))
    if coletar_idade <= 12:
        print('Usuário Criança')
    elif coletar_idade >= 13 and coletar_idade <= 17:
        print('Usuário Adolescente')
    elif coletar_idade >= 18:
        print('Usuário Adulto')
    else:
        print('Opção inválida')

def entrada():
    print('Insira o Nome e Senha')
    nome = str(input('Nome do Usuário: '))
    senha = str(input('Senha do Usuário: '))
    if nome == 'admin' and senha == '123':
        print('Bem vindo, Admin')
    else:
        print('Bem vindo, usuário')
def quadrante():
    x = float(input('Insira o valor de X: '))
    y = float(input('Insira o valor de Y: '))
    if x > 0 and y > 0:
        print('Primeiro Quadrante: os valores de x e y devem ser maiores que zero')
    elif x < 0 and y > 0:
        print('Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante: os valores de x e y devem ser menores que zero')
    elif x > 0 and y < 0:
        print('Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero')
    else:
        print('o ponto está localizado no eixo ou origem')
print('Bem vindo aos exercicios\nExercicio 1: Validador de Par ou Impar\nExercicio 2: Validador de Idade\nExercicio 3: Entrada de Usuário\nExercicio 4: Quadrando no Ponto Cartesiano')
opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        pares_impares()
    case 2:
        idades()
    case 3:
        entrada()
    case 4:
        quadrante()

    case _: 
        print('Opção inválida')


