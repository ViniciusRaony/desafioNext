from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/desafionext'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)
    activated = db.Column(db.Boolean, default=False)
    hash = db.Column(db.String(100))

    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email, "password": self.password,
                "activated": self.activated, "hash": self.hash}


# READ
@app.route("/users", methods=["GET"])
def select_users():
    users_objects = User.query.all()
    users_json = [user.to_json() for user in users_objects]  # Criando vetor para armazenar json
    return generate_response(200, "users", users_json, {})


@app.route("/user/<id>", methods=["GET"])
def select_user(id):
    user_object = User.query.filter_by(id=id).first()  # first() retorna o primeiro registro encontrado
    user_json = user_object.to_json()  # Sem for, busca por id individual
    return generate_response(200, "user", user_json)


# CREATE
@app.route("/user", methods=["POST"])
def create_user():
    body = request.get_json()
    try:
        user = User(name=body["name"], email=body["email"], password=body["password"], activated=body["activated"], hash=body["hash"])
        db.session.add(user)
        db.session.commit()
        return generate_response(201, "user", user.to_json(), "Cadastro criado com sucesso!")
    except Exception as e:
        print(e)
        return generate_response(400, "user", {}, "Erro ao criar cadastro")


# UPDATE
@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    user_object = User.query.filter_by(id=id).first()
    body = request.get_json()
    try:
        if 'name' in body:
            user_object.nome = body['name']
        if 'email' in body:
            user_object.email = body['email']
        if 'password' in body:
            user_object.email = body['password']
        if 'activated' in body:
            user_object.email = body['activated']
        if 'hash' in body:
            user_object.email = body['hash']
        db.session.add(user_object)
        db.session.commit()
        return generate_response(201, "user", user_object.to_json(), "Cadastro atualizado com sucesso!")
    except Exception as e:
        print("Erro", e)
        return generate_response(400, "user", {}, "Erro ao atualizar cadastro")


# DELETE
@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    user_object = User.query.filter_by(id=id).first()
    try:
        db.session.delete(user_object)
        db.session.commit()
        return generate_response(200, "user", user_object.to_json(), "Cadastro deletado com sucesso!")
    except Exception as e:
        print('Erro', e)
        return generate_response(400, "user", {}, "Erro ao deletar cadastro")


# GENERATE RESPONSE, OBS: Mensagem opcional
def generate_response(status, name_of_content, content, mensage=False):
    body = {}  # criando dicionário p/ retorno.
    body[name_of_content] = content

    if mensage:  # False ou zero
        body["message"] = mensage
    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()

'''
TODO
FLASK-EMAIL
MENSAGEM HASH PRA VALIDAR CRIAR ROTA GET P/ HASH: O status do usuario vai ficar false até ele clicar e validar)
ALTERAR STATUS NO BANCO DE DADOS: Depois que confirmar o email é que o status fica ativo, e ai ele pode fazer login
MENSAGEM DE NOTIFICAÇÃO: Não precisa mais validar no banco de dados, pois eu vou dar um usuarios.email && usuarios.status=TRUE
TEMPLATE HTML LOGIN
'''
