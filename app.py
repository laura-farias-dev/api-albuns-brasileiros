# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

albuns = [
    {"id": 1, "nome": "Clube da Esquina", "artista": "Milton Nascimento & Lô Borges", "ano": 1972},
    {"id": 2, "nome": "Acabou Chorare", "artista": "Novos Baianos", "ano": 1972}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/albuns', methods=['GET'])
def get_albuns():
    return jsonify(albuns)

@app.route('/api/albuns', methods=['POST'])
def create_album():
    data = request.get_json()
    novo_album = {
        "id": len(albuns) + 1,
        "nome": data.get("nome"),
        "artista": data.get("artista"),
        "ano": data.get("ano")
    }
    albuns.append(novo_album)
    return jsonify(novo_album), 201

@app.route('/api/albuns/<int:album_id>', methods=['PUT'])
def update_album(album_id):
    data = request.get_json()
    for album in albuns:
        if album['id'] == album_id:
            album['nome'] = data.get('nome', album['nome'])
            album['artista'] = data.get('artista', album['artista'])
            album['ano'] = data.get('ano', album['ano'])
            return jsonify(album), 200
    return jsonify({"error": "Álbum não encontrado"}), 404

@app.route('/api/albuns/<int:album_id>', methods=['DELETE'])
def delete_album(album_id):
    for i, album in enumerate(albuns):
        if album['id'] == album_id:
            deleted_album = albuns.pop(i)
            return jsonify({"message": "Álbum removido com sucesso", "album": deleted_album}), 200
    return jsonify({"error": "Álbum não encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
