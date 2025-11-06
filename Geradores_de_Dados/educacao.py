from faker import Faker
import random
import pandas as pd
import utils


fake = Faker("pt_BR")

def gerar_dados_educacao(qtd=100):
    #cursos e matérias base para criação de dados
    cursos = ["Administração", "Engenharia", "Direito", "Psicologia", "Sistemas de Informação"]
    materias = ["Matemática", "Português", "História", "Física", "Biologia"]

    dados = []

    #Iterar para crar linha por linha de dado
    for _ in range(qtd):
        dados.append({
            "Nome": fake.name(),
            "Curso": random.choice(cursos),
            "Matéria": random.choice(materias),
            "Nota Média": round(random.uniform(4, 10), 2),
            "Presença (%)": random.randint(50, 100),
            "Cidade": fake.city()
        })

    #Usa Panda para organizar dados em tabela
    return pd.DataFrame(dados)
