import os

restaurantes = ['Patos Food', 'Mac Ronalds']
def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o App...\n')
def opcao_invalida():
    print('Opção Inválida\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de Novos restaurantes\n')
    nome_do_restaurante = input('Insira o nome do restaurante para ser cadastrado: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()
def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes\n')
    for restaurante in restaurantes:
        print(f'-{restaurante}')
    input('Digite uma tecla para voltar ao menu principal')
    main()
def escolher_opcao():
    try:
        opcao = int(input('Insira uma opção: '))
        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            print('Ativar Restaurante')
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()