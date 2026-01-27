import os

restaurantes = ['Pizza Place', 'Sushi Bar', 'Burger Joint', 'Taco Restaurant']

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

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    if nome_restaurante in restaurantes:
        print('Restaurante já cadastrado. Tente novamente.\n')
        input('Pressione qualquer tecla para continuar... ')
        cadastrar_novo_restaurante()
    else:
        restaurantes.append(nome_restaurante)
        print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
        voltar_para_menu()

def listar_restaurantes():
    exibir_subtitulos('Listar restaurantes')
    for restaurante in restaurantes:
        print(f'Restaurante: {restaurante}\n')
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
            print('Ativar restaurante')
            nome = input('Digite o nome do restaurante a ser ativado: ')
            print(f'Restaurante {nome} ativado com sucesso!\n')
            return exibir_opcoes(), escolher_opcao()
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