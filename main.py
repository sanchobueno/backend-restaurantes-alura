import os

restaurantes = [{'nome': 'Pizza Place', 'categoria': 'Pizza', 'ativo': False},
                {'nome': 'Burger King', 'categoria': 'Americana', 'ativo': False},
                {'nome': 'Sushi Bar', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Taco Bell', 'categoria': 'Mexicana', 'ativo': False}]

def exebir_nome_programa():
    '''Exibe o nome do programa na tela'''
    print('''
┏━━━┓╋╋┏┓
┃┏━┓┃╋╋┃┃
┃┗━━┳━━┫┗━┳━━┳━┓┏━━┳┓┏┳━━┳━┳━━┳━━┳━━┓
┗━━┓┃┏┓┃┏┓┃┏┓┃┏┛┃┃━╋╋╋┫┏┓┃┏┫┃━┫━━┫━━┫
┃┗━┛┃┏┓┃┗┛┃┗┛┃┃╋┃┃━╋╋╋┫┗┛┃┃┃┃━╋━━┣━━┫
┗━━━┻┛┗┻━━┻━━┻┛╋┗━━┻┛┗┫┏━┻┛┗━━┻━━┻━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛
''')

def finalizar_app():
    '''finaliza o aplicativo'''
    exibir_subtitulos('Finalizando o aplicativo...')

def exibir_opcoes():
    '''exibe as opções do menu'''
    print('1 - cadastrar restaurante')
    print('2 - listar restaurante')
    print('3 - Alternar status restaurante')
    print('4 - sair\n')

def voltar_para_menu():
    '''volta para o menu'''
    input('Pressione ENTER para voltar ao menu... ')
    main()

def exibir_subtitulos(subtitulo):
    '''exibe os subtítulos'''
    os.system('cls')
    linha = '*' * len(subtitulo)
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def opcao_invalida():
    '''informa que a opção escolhida é inválida'''
    print('Opção inválida. Tente novamente.\n')
    voltar_para_menu()

def alterar_status_restaurante():
    '''altera o status do restaurante'''
    exibir_subtitulos('Alterar status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante para alternar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem_status = f' O restaurante {nome_restaurante} agora está {"ativo" if restaurante["ativo"] else "inativo"}.'
            print(mensagem_status)
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.')
        tentar_novamente = input('Tentar novamente? (S/N) ')
        if tentar_novamente.lower() == 's':
            alterar_status_restaurante()

    voltar_para_menu()

def cadastrar_novo_restaurante():
    '''cadastra um novo restaurante
    
    -Inputs: nome do restaurante, categoria do restaurante
    -Outputs: adiciona um novo restaurante a lista de restaurantes e exibe uma ensagem de sucesso ou erro
    '''
    exibir_subtitulos('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    if nome_restaurante in restaurantes:
        print('Restaurante já cadastrado. Tente novamente.\n')
        input('Pressione qualquer tecla para continuar... ')
        cadastrar_novo_restaurante()
    else:
        restaurantes.append(dados_restaurante)
        print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
        voltar_para_menu()

def listar_restaurantes():
    '''lista os restaurantes'''
    exibir_subtitulos('Listar restaurantes')
    print(f'{"Restaurante".ljust(22)} | {"Categoria".ljust(22)} | Status\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | - {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    print()
    voltar_para_menu()

def escolher_opcao():
    '''escolhe a opção do menu'''
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Opção escolhida: {opcao_escolhida}')
    try:
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()   
    except ValueError:
        opcao_invalida()
    
def main():
    '''função principal do programa'''
    os.system('cls')
    exebir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()