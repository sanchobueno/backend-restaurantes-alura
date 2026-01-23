import os
print('''
┏━━━┓╋╋┏┓
┃┏━┓┃╋╋┃┃
┃┗━━┳━━┫┗━┳━━┳━┓┏━━┳┓┏┳━━┳━┳━━┳━━┳━━┓
┗━━┓┃┏┓┃┏┓┃┏┓┃┏┛┃┃━╋╋╋┫┏┓┃┏┫┃━┫━━┫━━┫
┃┗━┛┃┏┓┃┗┛┃┗┛┃┃╋┃┃━╋╋╋┫┗┛┃┃┃┃━╋━━┣━━┃
┗━━━┻┛┗┻━━┻━━┻┛╋┗━━┻┛┗┫┏━┻┛┗━━┻━━┻━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛
      
      Bem-vindo ao sistema de cadastro de restaurantes!
''')

print('1 - cadastrar restaurante')
print('2 - listar restaurante')
print('3 - ativar restaurante')
print('4 - sair\n')

restaurantes = []

def finalizar_app():
    os.system('cls')
    print('Finalizando o aplicativo...\n')

opcao_escolhida = int(input('Escolha uma opção: '))
print(f'Opção escolhida: {opcao_escolhida}')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
    nome = input('Digite o nome do restaurante: ')
    restaurantes.append(nome)
    print(f'Restaurante {nome} cadastrado com sucesso!')
elif opcao_escolhida == 2:
    print('Listar restaurante')
    for restaurante in restaurantes:
        print(f'Restaurante: {restaurante}')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
    nome = input('Digite o nome do restaurante a ser ativado: ')
    print(f'Restaurante {nome} ativado com sucesso!')
elif opcao_escolhida == 4:
    finalizar_app()
else:
    print('Opção inválida. Tente novamente.')