empresas = []

while True:
    controle = input('Deseja cadastrar mais uma emrpesa: (s/n) ')
    if controle == 'n':
        break
    elif controle == 's':
        nome = input('Nome da empresa: ')
        cnpj = input('CNPJ (apenas dígitos): ')
        mfuncionarios = input('Quantidade de funcionários: ')
        mlucro = float(input('Lucro da empresa: '))
        empresa = Empresa(nome, cnpj, mfuncionarios, mlucro)
        empresas.append(empresa)
    else:
        print('Comando inválido!')
        continue

print('Informações sobre o prefeito:')
nome = input('Nome do prefeito: ')
cpf = input('CPF (apenas números): ')
formacao = input('Formação: ')
prefeito = Prefeito(nome, cpf, formacao)

print('Informações sobre a prefeitura:')
cidade = input('Cidade: ')
prefeitura = Prefeitura(cidade, prefeito.nome, empresas)

print(f'A prefeitura da cidade {prefeitura.cidade}, que tem {prefeito.nome} como prefeito(a), teve uma arrecadação total de R${prefeitura.TotalImpostos():.2f}')