from flask import Flask, jsonify

app = Flask(__name__)

albuns = [
    {"id": 1, "nome": "Clube da Esquina", "artista": "Milton Nascimento & Lô Borges", "ano": 1972},
    {"id": 2, "nome": "Acabou Chorare", "artista": "Novos Baianos", "ano": 1972}
]

@app.route('/api/albuns', methods=['GET'])
def get_albuns():
    return jsonify(albuns)

if __name__ == '__main__':
    app.run(debug=True)
