print('Cadastro de Usuario - Loja de Roupas Blah Blah\n')

def get_nome():
    while True:
        try:
            nome = input('Por favor, informe seu nome: ')
            if len(nome) >= 3:
                return nome
            elif nome.isnumeric():
                print('Erro: Números não são permitidos aqui.')
            else:
                print('Digite um nome maior/ou igual a 3 caracteres')
        except Exception:
            continue

def get_documento():
    while True:
        try:
            documento = input('Digite seu CPF/CNPJ(somente os números): ')
            if len(documento) == 11:
                cpf_format = (f"{documento[:3]}.{documento[3:6]}.{documento[6:9]}-{documento[9:]}")
                return cpf_format
            elif len(documento) == 14:
                cnpj_format = (f'{documento[:2]}.{documento[2:5]}.{documento[6:8]}/{documento[8:12]}-{documento[12:]}')
                return cnpj_format
            else:
                print('CPF/CNPJ inválido')
        except Exception:
            print('Erro: Letras não são permitidas aqui.')
            continue

def get_idade():
    while True:
        try:
            idade = int(input('Informe sua idade (somente os números): '))
            if idade >= 18:
                return idade
            else:
                print('A idade precisa ser maior ou igual a 18 anos')
        except Exception:
            print('Erro: Letras não são permitidas aqui.')
            continue

def get_salario():
    while True:
        try:
            salario = float(input('Informe seu salário: R$'))
            if salario > 0:
                return salario
            else:
                print('O salário precisa ser (pelo menos) maior que zero(0)')
        except Exception:
            print('Erro: Letras não são permitidas aqui.')
            continue

def get_sexo():
    parametro_sexo = ['m', 'f', 'M', 'F', 'o', 'O']
    while True:
        try:
            sexo = input('Informe seu sexo (M para Masculino, F para Feminino ou O para outro): ')
            if sexo in parametro_sexo:
                return sexo
            elif sexo.isnumeric():
                print('Erro: Números não são permitidos aqui.')
            else:
                print('Erro. Digite "M" para masculino, "F" para feminino ou "O" para outro')
        except Exception:
            continue

def get_estado_civil():
    parametro_est_civil = ['s', 'c', 'v', 'd', 'S', 'C', 'V', 'D']
    while True:
        try:
            est_civil = input('Digite S (Solteiro(a)), C (Casado(a)), V (Viuvo(a)), D (Divorciado(a)): ')
            if est_civil in parametro_est_civil:
                return est_civil
            elif est_civil.isnumeric():
                print('Erro: Números não são permitidos aqui.')
            else:
                print('Erro')
        except Exception:
            continue

def dados(nome, documento, idade, salario, sexo, est_civil):
    print('\nConfirme seus dados:')
    print(f'Nome: {nome.title()}')
    print(f'Documento: {documento}')
    print(f'Idade: {idade} anos')
    print(f'Salário: R${salario}')
    print(f'Sexo: {sexo.upper()}')
    print(f'Estado Civil: {est_civil.upper()}')

nome = get_nome()
documento = get_documento()
idade = get_idade()
salario = get_salario()
sexo = get_sexo()
est_civil = get_estado_civil()

dados(nome, documento, idade, salario, sexo, est_civil)

while True:
    try:
        choose = int(input('Deseja finalizar o cadastro? 1 (sim) 2 (editar): '))
        if choose == 1:
            print('Cadastro realizado com sucesso!')
            break
        elif choose == 2:
            nome = get_nome()
            documento = get_documento()
            idade = get_idade()
            sexo = get_sexo()
            salario = get_salario()
            est_civil = get_estado_civil()
            dados(nome, documento, idade, salario, sexo, est_civil)
    except Exception:
        continue



