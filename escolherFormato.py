from utils import salvar_excel, salvar_csv

def escolher_formato(df, nome_arquivo):
    print("\nEscolha o formato para salvar:")
    print("1 - CSV")
    print("2 - Excel (.xlsx)")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        salvar_csv(df, nome_arquivo)
    elif opcao == "2":
        salvar_excel(df, nome_arquivo)
    else:
        print("❌ Opção inválida! Salvando como CSV por padrão.")
        salvar_csv(df, nome_arquivo)
