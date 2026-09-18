import os

restaurantes = [{'nome': 'Patos Food', 'categoria': 'Comida Japonesa', 'ativo': False},
                {'nome': 'Mac Ronalds', 'categoria': 'Fast Food', 'ativo': True}
                ]

def exibir_nome_do_programa():
    '''
    Impremi o nome do projeto com uma fonte retirada do fsymbols
    '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    '''
    Exibi o menu de opções possuindo os números que o usuário pode colocar
    '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')
def voltar_ao_menu_principal():
    '''
    Retorna o usuário para o menu principal do Sabor Express
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    '''
    Limpa o terminal e em seguida adiciona asteristicos para enfeitar o resultado do terminal
    criando asteristicos de acordo com a quantidade do texto descrito
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
def finalizar_app():
    '''
    Retorna um texto de encerrando o app e fecha a aplicação
    '''
    exibir_subtitulo('Encerrando o App...')

def opcao_invalida():
    '''
    Retorna um erro de opção inválida e retorna para o menu principal e "reseta" a aplicação
    '''
    print('Opção Inválida\n')
    voltar_ao_menu_principal()
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    inputs: 
    - Nome do Restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de Novos restaurantes')
    print()
    nome_do_restaurante = input('Insira o nome do restaurante para ser cadastrado: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = { 'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()
    main()
def listar_restaurantes():
    '''
    Lista os restaurantes que estão cadastrados no dicionário retornando o nome, categoria e se está ativo ou desativo
    além disso apresenta nomes para substituir o True e False para Ativo e Desativo.
    Possui também o ljust que proporciona um espaço entre o código
    '''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status '}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''
    Alterna o estado do restaurante que o usuário informou

    inputs:
    Busca um restaurante dentro do dicionário e altera o estado dele
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante =  input('Digite o nome do restaurante que deseja alterar o estado:')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()
    main()
def escolher_opcao():
    '''
    Menu de informações 

    inputs:
    Usuário inseri a opção que ele quer no menu
    '''
    try:
        opcao = int(input('Insira uma opção: '))
        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alternar_estado_restaurante()
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    '''Inicia nosso projeto
    apaga o terminal, exibe o nome do programa, as opções e a lógica de escolha de opções
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()