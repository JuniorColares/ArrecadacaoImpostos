class Empresa:
    def __init__(self, nome, cnpj, mfuncionarios, mlucro):
        self.nome = nome
        self.cnpj = cnpj
        self.mfuncionarios = mfuncionarios
        self.mlucro = mlucro

class Prefeitura:
    def __init__(self, cidade, prefeito, empresas, timpostos = 0):
        self.cidade = cidade
        self.prefeito = prefeito
        self.empresas = empresas
        self.timpostos = timpostos

    def TotalImpostos(self):
        for empresa in self.empresas:
            self.timpostos += empresa.mlucro*0.016
        return self.timpostos

class Prefeito:
    def __init__(self, nome, cpf, formacao):
        self.nome = nome
        self.cpf = cpf
        self.formacao = formacao

import os

empresas = []

while True:
    controle = input('Deseja cadastrar mais uma emrpesa: (s/n) ')
    if controle == 'n':
        break
    elif controle == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        nome = input('Nome da empresa: ')
        cnpj = input('CNPJ (apenas dígitos): ')
        mfuncionarios = input('Quantidade de funcionários: ')
        mlucro = float(input('Lucro da empresa: '))
        empresa = Empresa(nome, cnpj, mfuncionarios, mlucro)
        empresas.append(empresa)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Comando inválido!')
        continue

os.system('cls' if os.name == 'nt' else 'clear')
print('Informações sobre o prefeito:')
nome = input('Nome do prefeito: ')
cpf = input('CPF (apenas números): ')
formacao = input('Formação: ')
prefeito = Prefeito(nome, cpf, formacao)

os.system('cls' if os.name == 'nt' else 'clear')
print('Informações sobre a prefeitura:')
cidade = input('Cidade: ')
prefeitura = Prefeitura(cidade, prefeito.nome, empresas)

os.system('cls' if os.name == 'nt' else 'clear')
print(f'A prefeitura da cidade {prefeitura.cidade}, que tem {prefeito.nome} como prefeito(a), teve uma arrecadação total de R${prefeitura.TotalImpostos():.2f}')