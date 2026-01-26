import os

restaurantes = []

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
      
      Bem-vindo ao sistema de cadastro de restaurantes!
''')

def finalizar_app():
    os.system('cls')
    print('Finalizando o aplicativo...\n')

def exibir_opcoes():
    print('1 - cadastrar restaurante')
    print('2 - listar restaurante')
    print('3 - ativar restaurante')
    print('4 - sair\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Opção escolhida: {opcao_escolhida}')

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
        nome = input('Digite o nome do restaurante: ')
        restaurantes.append(nome)
        print(f'Restaurante {nome} cadastrado com sucesso!\n')
        return exibir_opcoes(), escolher_opcao()
    elif opcao_escolhida == 2:
        print('Listar restaurante')
        for restaurante in restaurantes:
            print(f'Restaurante: {restaurante}\n')
        return exibir_opcoes(), escolher_opcao()
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
        nome = input('Digite o nome do restaurante a ser ativado: ')
        print(f'Restaurante {nome} ativado com sucesso!\n')
        return exibir_opcoes(), escolher_opcao()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        print('Opção inválida. Tente novamente.\n')
        return exibir_opcoes(), escolher_opcao()
    
def main():
    exebir_nome_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()