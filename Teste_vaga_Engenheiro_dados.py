import pandas as pd

import re




# Função para limpar e normalizar CPFs

def limpar_cpf(cpf):

    # Remover caracteres especiais e deixar apenas dígitos

    cpf = re.sub(r'\D', '', cpf)

    return cpf


# Função para limpar e normalizar CNPJs

def limpar_cnpj(cnpj):

    # Remover caracteres especiais e deixar apenas dígitos

    cnpj = re.sub(r'\D', '', cnpj)

    return cnpj
    

# Função para verificar se um CPF é válido

def validar_cpf(cpf):

    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11:

        return True

    elif cpf == cpf[0] * 11:

        return False

    else:

        cpf = list(map(int, cpf))

        soma1 = sum(cpf[i] * (10 - i) for i in range(9)) * 10

        resto1 = soma1 % 11

        if resto1 == 10:

            resto1 = 0

        soma2 = sum(cpf[i] * (11 - i) for i in range(10)) * 10

        resto2 = soma2 % 11

        if resto2 == 10:

            resto2 = 0

        if resto1 == cpf[9] and resto2 == cpf[10]:

            return True

        else:

            return False

 

# Função para verificar se um CNPJ é válido

def validar_cnpj(cnpj):

    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")

    if len(cnpj) != 14:

        return True

    elif cnpj == cnpj[0] * 14:

        return False

    else:

        cnpj = list(map(int, cnpj))

        soma1 = sum(cnpj[i] * (5 - i if i < 4 else 12 - i) for i in range(12)) % 11

        digito1 = 0 if soma1 < 2 else 11 - soma1

        soma2 = sum(cnpj[i] * (6 - i if i < 5 else 13 - i) for i in range(13)) % 11

        digito2 = 0 if soma2 < 2 else 11 - soma2

        if digito1 == cnpj[12] and digito2 == cnpj[13]:

            return True

        else:

            return False

# Leitura do arquivo CSV
df = pd.read_csv('dados_cadastrais_fake.csv', sep = ";")

df['cpf'] = df['cpf'].apply(limpar_cpf)

df['cnpj'] = df['cnpj'].apply(limpar_cnpj)

# Adicionar colunas de CPF e CNPJ válidos



# Verificando a quantidade de clientes na base
num_clientes = df.shape[0]
print("Quantidade de clientes na base: ", num_clientes)

media_idade = df['idade'].mean()
print("Média de idade dos clientes: ", media_idade)

clientes_por_estado = df['estado'].value_counts()
print("Quantidade de clientes por estado:\n", clientes_por_estado)

df['qtd_clientes_estado'] = df['estado'].map(clientes_por_estado)
df['media_idade'] = media_idade

df["CPF_Valido_Invalido"] = df["cpf"].apply(validar_cpf)

df["CNPJ_Valido_Invalido"] = df["cnpj"].apply(validar_cnpj)

df["Quantidade CPF Válidos"] = df["CPF_Valido_Invalido"] .sum()

df["Quantidade de CPF Inválidos"] = len(df)-df["Quantidade CPF Válidos"]

df["Quantidade CNPJ Válidos"] = df["CNPJ_Valido_Invalido"] .sum()

df["Quantidade de CNPJ Inválidos"] = len(df)-df["Quantidade CNPJ Válidos"]

df['Quantidade_Clientes'] = df.shape[0]


df.to_csv('problema1_normalizado.csv', index=False)
df.to_parquet('problema1_normalizado.parquet', index=False)

# Limpar e normalizar CPFs e CNPJs


