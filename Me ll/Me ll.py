import pandas as pd
import datetime as dt

def atualizar_base(df,nome_banco):
    df.to_excel(nome_banco,index=False)

profs_df = pd.read_excel('Professores.xlsx')
alunos_df = pd.read_excel('Alunos.xlsx')
disciplinas_df = pd.read_excel('Disciplinas.xlsx')
faltas_df = pd.read_excel('Faltas.xlsx')


while True:
    print('''
============== MENU ==============

1-Cadastro De Professores
2-Cadastro De Alunos
3-Cadastro De Disciplinas
4-Cadastro De faltas
5-Relatoria de falhas\n''')

    opçao = int(input('Digite a opção Desejada: '))

    if opçao == 1:
        nome = (input('Nome: '))
        matricula = int(input('Matricula: '))
        print('Informe Sua Data de Nascimento. Ex: (Dia:12 Mes:07 Ano:2003')
        dia = int(input('Dia: '))
        mes = int(input('Mês: '))
        ano = int(input('Ano: '))

        date = dt.datetime(ano, mes, dia)

        linha = [nome,matricula,date]
        profs_df.loc[len(profs_df)] = linha
        atualizar_base(profs_df,'Professores.xlsx')

    if opçao == 2:
        nome = (input('Nome: '))
        matricula = int(input('Matricula: '))
        print('Informe Sua Data de Nascimento. Ex: (Dia: 12 Mes:07 Ano:2003')
        dia = int(input('Dia: '))
        mes = int(input('Mês: '))
        ano = int(input('Ano: '))

        date = dt.datetime(ano, mes, dia)

        linha = [nome,matricula,date]
        alunos_df.loc[len(alunos_df)] = linha
        atualizar_base(alunos_df,'Alunos.xlsx')


    if opçao == 3:
        matricula = int(input('Matricula do Professor: '))
        if matricula in profs_df.Matricula_Professor.values:
            nome = input('Nome da Disciplina: ')
            codigo = int(input('Código da Disciplina: '))
        else:
            print('Matricula Inexistente!')
            continue

        linha = [codigo,nome, matricula]
        disciplinas_df.loc[len(disciplinas_df)] = linha
        atualizar_base(disciplinas_df,'Disciplinas.xlsx')


    if opçao == 4:
        codigo = int(input('Informe o Código da Disciplina: '))
        matricula = int(input('Matricula do Aluno: '))
        if codigo in disciplinas_df.Código.values and matricula in alunos_df.Matricula_Aluno.values:
            presenca = (input('Presença: '))
        else:
            print('Matricula Inexistente!')
            continue

        linha = [codigo,matricula,presenca]
        faltas_df.loc[len(faltas_df)] = linha
        atualizar_base(faltas_df,'Faltas.xlsx')

    if opçao == 5:
        codigo = int(input('Informe o Código da Disciplina: '))
        if codigo in disciplinas_df.Código.values:
            if codigo == disciplinas_df.Código.values[0]:
                print(f'Disciplina: {disciplinas_df.Nome.values[0]}')
                print(f'Professor: {profs_df.Nome.values[0]}')
                print(f'Alunos: {alunos_df.Nome.values}')
                print(f'Presença: {faltas_df.Presença.values}')
            if codigo == disciplinas_df.Código.values[1]:
                print(f'Disciplina: {disciplinas_df.Nome.values[1]}')
                print(f'Professor: {profs_df.Nome.values[1]}')
                print(f'Alunos: {alunos_df.Nome.values}')
                print(f'Presença: {faltas_df.Presença.values}')
            if codigo == disciplinas_df.Código.values[2]:
                print(f'Disciplinas : {disciplinas_df.Nome.values[2]}')
                print(f'Professor: {profs_df.Nome.values[0]}')
                print(f'Alunos: {alunos_df.Nome.values}')
                print(f'Presença: {faltas_df.Presença.values}')

            if codigo == disciplinas_df.Código.values[3]:
                print(f'Disciplina: {disciplinas_df.Nome.values[3]} ')
                print(f'Professor: {profs_df.Nome.values[0]}')
                print(f'Alunos: {alunos_df.Nome.values}')
                print(f'Presença: {faltas_df.Presença.values}')


        else:
            print('Codigo De Matricula Inexistente!')
            continue


    parada = input('Deseja continuar? [S/N]: ')
    if parada in 'Nn':
        break