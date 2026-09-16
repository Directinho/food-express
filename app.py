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
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
def finalizar_app():
    exibir_subtitulo('Encerrando o App...')
    print()
def opcao_invalida():
    print('Opção Inválida\n')
    voltar_ao_menu_principal()
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novos restaurantes')
    print()
    nome_do_restaurante = input('Insira o nome do restaurante para ser cadastrado: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()
    main()
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print()
    for restaurante in restaurantes:
        print(f'-{restaurante}')
    voltar_ao_menu_principal()
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