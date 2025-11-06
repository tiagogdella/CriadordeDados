import os

def salvar_csv(df, nome_arquivo):
    """Salva o Dado em um arquivo CSV dentro da pasta dadosExcel/"""
    os.makedirs("dadosExcel", exist_ok=True)
    caminho = f"dadosExcel/{nome_arquivo}.csv"
    df.to_csv(caminho, index=False, encoding="utf-8-sig")
    print(f"✅ Arquivo salvo em: {caminho}")
