import pandas as pd

cont = {'': 0}

def atualizar_base(df,nome_banco):
    df.to_excel(nome_banco,index=False)

vendedor_df = pd.read_excel('Vendedor.xlsx')
maquinas_df = pd.read_excel('Maquinas.xlsx')
clientes_df = pd.read_excel('Clientes.xlsx')

def Vendedor():
    nome = input('Nome: ')
    cpf = int(input('Cpf: '))
    data_nascimento = int(input('Data de nascimento: '))
    endereco = (input('Endereço: '))

    linha = [nome, cpf, data_nascimento, endereco]
    vendedor_df.loc[len(vendedor_df)] = linha
    atualizar_base(vendedor_df, 'Vendedor.xlsx')

    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco



def Maquinas():
    codigo = int(input('Codigo Da Maquina: '))
    descricao = input('Descrição Da Maquina: ')
    preço_unitario = int(input('Preço Unitario: '))
    estoque = int(input('Quantidade No estoque: '))
    list0 = list(cont.values())
    contador1 = list(cont.keys())
    contador2 = list(cont.values())

    linha = [codigo, descricao, preço_unitario, cont]
    maquinas_df.loc[len(maquinas_df)] = linha
    atualizar_base(maquinas_df, 'Maquinas.xlsx')

    def __init__(self, codigo, descricao, preço_unitario, estoque):
        self.codigo = codigo
        self.descricao = descricao
        self.preço_unitario = preço_unitario
        self.estoque = estoque


def Clientes():
    nome = input('Nome: ')
    cpf = int(input('Cpf: '))
    data_nascimento = int(input('Data de nascimento: '))
    endereco = (input('Endereço: '))

    linha = [nome, cpf, data_nascimento, endereco]
    clientes_df.loc[len(clientes_df)] = linha
    atualizar_base(clientes_df, 'Clientes.xlsx')

    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco



