from faker import Faker
import random
import pandas as pd
from datetime import timedelta
import utils


fake = Faker("pt_BR")

def gerar_dados_vendas(qtd=100):
    #cursos e matérias base para criação de dados
    produtos = ["Notebook", "Celular", "Fone de Ouvido", "Monitor", "Teclado", "Mouse"]
    categorias = ["Eletrônicos", "Acessórios", "Informática"]
    dados = []

    #Iterar para crar linha por linha de dado
    for _ in range(qtd):
        produto = random.choice(produtos)
        categoria = random.choice(categorias)
        preco = round(random.uniform(50, 5000), 2)
        quantidade = random.randint(1, 10)
        total = round(preco * quantidade, 2)
        data_venda = fake.date_between(start_date="-1y", end_date="today")

        dados.append({
            "Produto": produto,
            "Categoria": categoria,
            "Preço Unitário": preco,
            "Quantidade": quantidade,
            "Total": total,
            "Data da Venda": data_venda,
            "Cidade": fake.city()
        })

    #Usa Panda para organizar dados em tabela
    return pd.DataFrame(dados)
