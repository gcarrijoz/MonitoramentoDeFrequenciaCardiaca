from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para receber dados do ESP32
@app.route('/dados', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON inválido"}), 400

    print(f"Dados recebidos: {dados}")
    return jsonify({"status": "sucesso", "mensagem": "Dado recebido"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
