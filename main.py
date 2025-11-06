from Geradores_de_Dados.educacao import gerar_dados_educacao
from Geradores_de_Dados.vendas import gerar_dados_vendas
from Geradores_de_Dados.rh import gerar_dados_rh
from utils import salvar_csv

def menu():
    while True:
        print("\n📊 GERADOR DE DATASETS PARA ANÁLISE DE DADOS 📊")
        print("1 - Dados Educacionais")
        print("2 - Dados de Vendas")
        print("3 - Dados de Recursos Humanos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao in ["1", "2", "3"]:
            qtd = int(input("Quantas linhas deseja gerar? "))

            if opcao == "1":
                df = gerar_dados_educacao(qtd)
                nome = "educacao"
            elif opcao == "2":
                df = gerar_dados_vendas(qtd)
                nome = "vendas"
            elif opcao == "3":
                df = gerar_dados_rh(qtd)
                nome = "rh"

            print(df.head())
            salvar_csv(df, f"{nome}_{qtd}_linhas")

        elif opcao == "0":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    menu()
