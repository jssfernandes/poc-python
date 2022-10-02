from fastapi import FastAPI

app = FastAPI()

pessoas = {
    1: {"id": 1, "first_name": "Charin", "last_name": "Corrado", "email": "ccorrado0@google.cn"},
    2: {"id": 2, "first_name": "Ardelia", "last_name": "Antuoni", "email": "aantuoni1@mapy.cz"},
    3: {"id": 3, "first_name": "Maribeth", "last_name": "Winridge", "email": "mwinridge2@abc.net.au"},
    4: {"id": 4, "first_name": "Johnnie", "last_name": "Odde", "email": "jodde3@youku.com"},
}

@app.get("/")
def home():
    return {"quantidade_pessoas": len(pessoas)}

@app.get("/pessoas/{id_pessoa}")
def get_pessoa(id_pessoa: int):
    if id_pessoa in pessoas:
        return pessoas[id_pessoa]
    else:
        return {"Erro": "ID inexistente"}

# para executar o fastapi basta executar o 'uvicorn + nome_arquivo + nome_aplicacao' conforme o exemplo abaixo
# uvicorn api:app --reload

# para acessar a doc do api acessar a rota
# host:porta/docs