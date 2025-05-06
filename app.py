from flask import Flask, jsonify, request

app = Flask(__name__)

albuns = [
    {"id": 1, "nome": "Clube da Esquina", "artista": "Milton Nascimento & Lô Borges", "ano": 1972},
    {"id": 2, "nome": "Acabou Chorare", "artista": "Novos Baianos", "ano": 1972}
]

@app.route('/api/albuns', methods=['GET', 'POST'])
def albuns_handler():
    if request.method == 'GET':
        return jsonify(albuns)
    elif request.method == 'POST':
        data = request.get_json()
        novo_album = {
            "id": len(albuns) + 1,
            "nome": data.get("nome"),
            "artista": data.get("artista"),
            "ano": data.get("ano")
        }
        albuns.append(novo_album)
        return jsonify(novo_album), 201
