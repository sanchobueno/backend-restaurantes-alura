import os

restaurantes = [{'nome': 'Pizza Place', 'categoria': 'Pizza', 'ativo': False},
                {'nome': 'Burger King', 'categoria': 'Americana', 'ativo': False},
                {'nome': 'Sushi Bar', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Taco Bell', 'categoria': 'Mexicana', 'ativo': False}]

def exebir_nome_programa():
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
    exibir_subtitulos('Finalizando o aplicativo...')

def exibir_opcoes():
    print('1 - cadastrar restaurante')
    print('2 - listar restaurante')
    print('3 - ativar restaurante')
    print('4 - sair\n')

def voltar_para_menu():
    input('Pressione qualquer tecla para voltar ao menu... ')
    main()

def exibir_subtitulos(subtitulo):
    os.system('cls')
    print(subtitulo)
    print()

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    voltar_para_menu()

def alterar_status_restaurante():
    exibir_subtitulos('Alterar status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante para alternar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem_status = f' O restaurante {nome_restaurante} agora está {"ativo" if restaurante["ativo"] else "inativo"}.'
            print(mensagem_status)
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.')

    voltar_para_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input('Digite a categoria do restaurante: ')
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
    exibir_subtitulos('Listar restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f'Restaurante: {nome_restaurante} | Categoria: {categoria_restaurante} | Ativo: {ativo_restaurante}\n')
    voltar_para_menu()

def escolher_opcao():
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
    os.system('cls')
    exebir_nome_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()