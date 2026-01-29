import os
from modelos.restaurantes import Restaurante


restaurantes = [Restaurante('Praça', 'Comida caseira'),
                Restaurante('Juca Brazuca', 'Comida brasileira'),
                Restaurante('Sushi Sushiaki', 'Comida japonesa'),
                Restaurante('Pizza Lust', 'pizza')
                ]

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

def verificar_restaurante_existente(nome_restaurante):
    '''verifica se o restaurante já existe'''
    while not nome_restaurante.lower() in [restaurante._nome.lower() for restaurante in Restaurante.restaurantes]:
        print(f'Restaurante {nome_restaurante} não encontrado.')
        nome_restaurante = input('Tente novamente ou pressione N para voltar ao menu: ')
        if nome_restaurante.lower() == 'n':
            voltar_para_menu()
    else:
        print(f'Restaurante {nome_restaurante} encontrado.')
        return nome_restaurante        

def finalizar_app():
    '''finaliza o aplicativo'''
    exibir_subtitulos('Finalizando o aplicativo...')

def exibir_opcoes():
    '''exibe as opções do menu'''
    print('1 - cadastrar restaurante')
    print('2 - listar restaurante')
    print('3 - Alternar status restaurante')
    print('4 - Avaliar restaurante')
    print('5 - Sair\n')

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
    nome_restaurante = verificar_restaurante_existente(input('Digite o nome do restaurante que deseja alterar o status: '))
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome_restaurante:
            novo_status = restaurante.alternar_status()
            print(f'Status do restaurante {restaurante._nome} alterado para {novo_status}.\n')

    voltar_para_menu()

def cadastrar_novo_restaurante():
    '''cadastra um novo restaurante
    
    -Inputs: nome do restaurante, categoria do restaurante
    -Outputs: adiciona um novo restaurante a lista de restaurantes e exibe uma ensagem de sucesso ou erro
    '''
    exibir_subtitulos('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    if nome_restaurante.lower() in [restaurante._nome.lower() for restaurante in Restaurante.restaurantes]:
        print('Restaurante já cadastrado. Tente novamente.\n')
        input('Pressione qualquer tecla para continuar... ')
        cadastrar_novo_restaurante()
    else:
        categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
        dados_restaurante = Restaurante(nome_restaurante, categoria_restaurante)
        restaurantes.append(dados_restaurante)
        print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
        voltar_para_menu()

def avaliar_restaurante():
    '''avalia o restaurante'''
    exibir_subtitulos('Avaliar restaurante')
    nome_restaurante = verificar_restaurante_existente(input('Digite o nome do restaurante que deseja avaliar: '))
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome_restaurante:
            cliente = input('Digite seu nome: ')
            while True:
                try:
                    nota = float(input('Digite a nota (0 a 5): '))
                    if nota < 0 or nota > 5:
                        raise ValueError
                    break
                except ValueError:
                    print('Nota inválida. Digite um número entre 0 e 5.')
            comentario = input('Digite um comentário (opcional): ')
            restaurante.receber_avaliacao(cliente, nota, comentario)
            print('Avaliação registrada com sucesso!')
            voltar_para_menu()

def listar_restaurantes():
    '''lista os restaurantes'''
    exibir_subtitulos('Listar restaurantes')
    Restaurante.listar_restaurantes()
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
            avaliar_restaurante()
        elif opcao_escolhida == 5:
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