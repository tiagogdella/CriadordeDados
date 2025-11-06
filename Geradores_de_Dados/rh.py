from faker import Faker
import random
import pandas as pd
from datetime import date
import utils

fake = Faker("pt_BR")

def gerar_dados_rh(qtd=100):
    #cursos e matérias base para criação de dados
    cargos = ["Analista", "Gerente", "Técnico", "Assistente", "Estagiário"]
    setores = ["Financeiro", "RH", "Marketing", "TI", "Produção"]

    dados = []

    #Iterar para crar linha por linha de dado
    for _ in range(qtd):
        salario = round(random.uniform(1800, 15000), 2)
        admissao = fake.date_between(start_date="-5y", end_date="today")
        tempo_empresa = (date.today() - admissao).days // 365

        dados.append({
            "Nome": fake.name(),
            "Idade": random.randint(20, 60),
            "Cargo": random.choice(cargos),
            "Setor": random.choice(setores),
            "Salário (R$)": salario,
            "Tempo de Empresa (anos)": tempo_empresa
        })

    #Usa Panda para organizar dados em tabela
    return pd.DataFrame(dados)
