from flask import Flask, request, send_file, jsonify
import pandas as pd
import io
from Geradores_de_Dados import gerar_dados  # importa tua função geradora

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "API do Gerador de Dados está online!"})

@app.route('/gerar', methods=['POST'])
def gerar():
    try:
        data = request.get_json()
        tipo = data.get('tipo', 'padrao')
        linhas = int(data.get('linhas', 10))

        df = gerar_dados(tipo, linhas)

        # salva CSV em memória
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)

        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            download_name=f"{tipo}_dados.csv"
        )
    except Exception as e:
        return jsonify({"erro": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
