import pandas as pd


def atualizar_base(df,nome_banco):
    df.to_excel(nome_banco, index=False)


vendedor_df = pd.read_excel('Vendedor.xlsx')
maquinas_df = pd.read_excel('Maquinas.xlsx')
clientes_df = pd.read_excel('Clientes.xlsx')
vendas_df = pd.read_excel('Vendas.xlsx')


def Vendas():
    while True:
        codigo_da_venda = int(input('Codigo da venda: '))
        cpf_vendedor = int(input('Cpf do Vendedor: '))
        if cpf_vendedor in vendedor_df.Cpf.values:
            data_venda = int(input('Data da Venda: '))
            codigo_da_maquina = int(input('Informe o Codigo da Maquina: '))
            if codigo_da_maquina in maquinas_df.Codigo.values:
                qtd_vendida = int(input('Quantidades a serem Compradas: '))
            else:
                print('Codigo Inexistente!')
                print('Informe os dados novamente!\n')
                continue
        else:
            print('CPF Inexistente!')
            print('Informe os dados novamente!\n')
            continue

        linha = [codigo_da_venda, cpf_vendedor, data_venda, codigo_da_maquina, qtd_vendida]
        vendas_df.loc[len(vendas_df)] = linha
        atualizar_base(vendas_df, 'Vendas.xlsx')

        parada = input('Deseja Adicionar outro Item[S/N]: ')
        if parada in 'Nn':
            break


def Relatorio_de_vendas():
    cont = -1
    while True:
        cont = cont + 1
        print(f'Codigo da Venda: {vendas_df.Codigo_Da_Venda.values[cont]} ')
        print(f'Data da Venda: {vendas_df.Data_Da_Venda.values[cont]}')
        print(f'Nome do Vendedor: {vendedor_df.Nome.values[cont]}')
        print(f'Nome do Cliente: {clientes_df.Nome.values[cont]}')
        print(f'Valor Total Da Venda: {maquinas_df.Estoque.values[cont] * maquinas_df.Preço.values[cont]}')
        print(f'''
        Descrição Da Maquina       Quantidade Vendida       Preço Unitario       Valor Total Item
        {maquinas_df.Descrição.values[cont]}                      {vendas_df.Quantidade_Vendida.values[cont]}                        {maquinas_df.Preço.values[cont]}                   {maquinas_df.Estoque.values[cont] * maquinas_df.Preço.values[cont]}''')
        parada = input('Deseja ver mais Relatorios? ')
        print()
        if parada in 'Nn':
            break


def Relatorio_Comissao():
    cont = -1
    while True:
        cont = cont + 1
        print(f'Codigo da Venda: {vendas_df.Codigo_Da_Venda.values[cont]} ')
        print(f'Data da Venda: {vendas_df.Data_Da_Venda.values[cont]}')
        print(f'Nome do Vendedor: {vendedor_df.Nome.values[cont]}')
        print(f'Valor Total Da Venda: {maquinas_df.Estoque.values[cont] * maquinas_df.Preço.values[cont]}')
        print(f'Valor Da Comissão: {(maquinas_df.Estoque.values[cont] * maquinas_df.Preço.values[cont]) * 0.1}')
        parada = input('Deseja ver mais Relatorios De Comissao? ')
        print()
        if parada in 'Nn':
            break
