import firebase_admin
from firebase_admin import credentials, firestore

# Substitua pelo caminho para o seu arquivo de credenciais JSON
cred = credentials.Certificate(r"C:\Users\marco\OneDrive\Área de Trabalho\sla\p2bancodedados-firebase-adminsdk-demew-7050a832de.json")
firebase_admin.initialize_app(cred)

# Obtenha uma referência para o Firestore
db = firestore.client()

# Dados a serem inseridos
mangas = [
    {"id": "1", "titulo": "Naruto", "autor": "Masashi Kishimoto", "ano": 1999, "genero": "Ação/Aventura", "vendas": 250000000},
    {"id": "2", "titulo": "One Piece", "autor": "Eiichiro Oda", "ano": 1997, "genero": "Ação/Aventura", "vendas": 517000000},
    {"id": "3", "titulo": "Attack on Titan", "autor": "Hajime Isayama", "ano": 2009, "genero": "Ação/Drama", "vendas": 100000000},
    {"id": "4", "titulo": "Dragon Ball", "autor": "Akira Toriyama", "ano": 1984, "genero": "Ação/Aventura", "vendas": 250000000},
    {"id": "5", "titulo": "Death Note", "autor": "Tsugumi Ohba", "ano": 2003, "genero": "Suspense/Psicologia", "vendas": 30000000}
]

livros = [
    {"id": "1", "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "genero": "Fantasia", "vendas": 150000000},
    {"id": "2", "titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Distopia", "vendas": 30000000},
    {"id": "3", "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "genero": "Satira", "vendas": 25000000},
    {"id": "4", "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "genero": "Fantasia", "vendas": 140000000},
    {"id": "5", "titulo": "Cem Anos de Solidão", "autor": "Gabriel Garcia Marquez", "ano": 1967, "genero": "Realismo Mágico", "vendas": 50000000}
]

# Função para adicionar dados ao Firestore
def adicionar_dados(collection_name, data):
    collection_ref = db.collection(collection_name)
    for item in data:
        collection_ref.add(item)
    print(f"Dados adicionados à coleção {collection_name}")

# Adiciona mangás e livros ao Firestore
adicionar_dados('mangas', mangas)
adicionar_dados('livros', livros)

print("Dados inseridos com sucesso!")
