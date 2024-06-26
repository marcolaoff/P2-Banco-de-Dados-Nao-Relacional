# P2-Banco-de-Dados-Nao-Relacional
# Biblioteca API com Firestore

Este projeto consiste em uma API desenvolvida com Flask que interage com o Firestore, um banco de dados NoSQL em tempo real, parte do Firebase. A API permite realizar operações CRUD (Create, Read, Update, Delete) para coleções de mangás e livros.

## Descrição Técnica

**Firestore** é um banco de dados NoSQL flexível e escalável que armazena dados em documentos organizados em coleções. Ele suporta atualizações em tempo real e oferece consultas ricas e indexação automática. É ideal para aplicações que requerem sincronização em tempo real e escalabilidade.

## Configuração

### Requisitos Mínimos

- Conta no Google Firebase.
- Acesso à internet.
- Ferramenta de desenvolvimento como Postman ou navegador moderno.

### Requisitos Recomendados

- IDE como PyCharm ou Visual Studio Code.
- Ambiente Python configurado com as bibliotecas necessárias (`firebase-admin`, `Flask`).
- Conta no Google Cloud Platform para gerenciamento avançado.

## Instalação

### Passos para Configuração do Firestore

1. **Criar um Projeto no Firebase**:
   - Acesse [Firebase Console](https://console.firebase.google.com/).
   - Crie um novo projeto ou use um projeto existente.

2. **Habilitar Firestore**:
   - No console do Firebase, selecione o projeto.
   - Clique em "Firestore Database" e configure o Firestore.

3. **Obter Credenciais**:
   - Vá para "Configurações do Projeto" -> "Contas de Serviço".
   - Clique em "Gerar nova chave privada" e baixe o arquivo JSON.

