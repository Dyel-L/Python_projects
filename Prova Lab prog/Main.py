import pandas as pd
import Cadastros
import Vendas
while True:
    print('''

=============== MENU ===============

[1] Cadastrar Vendedor
[2] Cadastrar Máquinas
[3] Cadastrar Clientes
[4] Registrar Venda
[5] Relatorio De Vendedores
[6] Relatorio De Máquinas
[7] Relatorio De Clientes
[8] Relatorio De Vendas
[9] Relatorio De Comissoes''')
    print()

    opcao = int(input('Qual a opção desejada?: '))
    print()

    if opcao == 1:
        Cadastros.Vendedor()

    if opcao == 2:
        Cadastros.Maquinas()

    if opcao == 3:
        Cadastros.Clientes()

    if opcao == 4:
        Vendas.Vendas()

    if opcao == 5:
        try:
                print(pd.read_excel('Vendedor.xlsx'))
        except FileNotFoundError:
                print("\nNão Tem Maquinas Cadastradas!\n")

    if opcao == 6:
        try:
                print(pd.read_excel('Maquinas.xlsx'))
        except FileNotFoundError:
                print("\nNão Tem Maquinas Cadastradas!\n")

    if opcao == 7:
        try:
                print(pd.read_excel('Clientes.xlsx'))
        except FileNotFoundError:
                print("\nNão Tem Maquinas Cadastradas!\n")

    if opcao == 8:
        try:
            Vendas.Relatorio_de_vendas()
        except IndexError:
            print('Não Ha mais Relatorios De Vendas!')


    if opcao == 9:
        try:
            Vendas.Relatorio_Comissao()
        except IndexError:
            print('Não Ha mais Relatorios De Comissão!')

    parada = (input('Deseja continuar?[S/N]: '))

    if parada in 'Nn':
        break


