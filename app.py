from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import config

app = Flask(__name__)

# Inicializar o Firestore
cred = credentials.Certificate(config.FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Funções utilitárias para Firestore
def adicionar_dados(collection_name, data):
    collection_ref = db.collection(collection_name)
    doc_ref = collection_ref.document(data.get("id"))
    doc_ref.set(data)

def obter_dados(collection_name):
    collection_ref = db.collection(collection_name)
    docs = collection_ref.stream()
    return [doc.to_dict() for doc in docs]

def obter_dado_por_id(collection_name, doc_id):
    collection_ref = db.collection(collection_name)
    doc = collection_ref.document(doc_id).get()
    return doc.to_dict() if doc.exists else None

def atualizar_dados(collection_name, doc_id, data):
    collection_ref = db.collection(collection_name)
    doc_ref = collection_ref.document(doc_id)
    doc_ref.update(data)

def deletar_dados(collection_name, doc_id):
    collection_ref = db.collection(collection_name)
    doc_ref = collection_ref.document(doc_id)
    doc_ref.delete()

# Rotas para a coleção 'mangas'
@app.route('/mangas', methods=['POST'])
def add_manga():
    data = request.json
    adicionar_dados('mangas', data)
    return jsonify(message="Mangá adicionado com sucesso!"), 201

@app.route('/mangas', methods=['GET'])
def get_mangas():
    result = obter_dados('mangas')
    return jsonify(result), 200

@app.route('/mangas/<id>', methods=['GET'])
def get_manga(id):
    manga = obter_dado_por_id('mangas', id)
    if manga:
        return jsonify(manga), 200
    else:
        return jsonify(message="Mangá não encontrado"), 404

@app.route('/mangas/<id>', methods=['PUT'])
def update_manga(id):
    data = request.json
    atualizar_dados('mangas', id, data)
    return jsonify(message="Mangá atualizado com sucesso!"), 200

@app.route('/mangas/<id>', methods=['DELETE'])
def delete_manga(id):
    deletar_dados('mangas', id)
    return jsonify(message="Mangá deletado com sucesso!"), 200

# Rotas para a coleção 'livros'
@app.route('/livros', methods=['POST'])
def add_livro():
    data = request.json
    adicionar_dados('livros', data)
    return jsonify(message="Livro adicionado com sucesso!"), 201

@app.route('/livros', methods=['GET'])
def get_livros():
    result = obter_dados('livros')
    return jsonify(result), 200

@app.route('/livros/<id>', methods=['GET'])
def get_livro(id):
    livro = obter_dado_por_id('livros', id)
    if livro:
        return jsonify(livro), 200
    else:
        return jsonify(message="Livro não encontrado"), 404

@app.route('/livros/<id>', methods=['PUT'])
def update_livro(id):
    data = request.json
    atualizar_dados('livros', id, data)
    return jsonify(message="Livro atualizado com sucesso!"), 200

@app.route('/livros/<id>', methods=['DELETE'])
def delete_livro(id):
    deletar_dados('livros', id)
    return jsonify(message="Livro deletado com sucesso!"), 200

if __name__ == '__main__':
    app.run(debug=True)
