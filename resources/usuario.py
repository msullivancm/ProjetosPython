from flask_restful import Resource, reqparse
from models.usuarios import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
import hmac
str_to_bytes = lambda s: s.encode("utf-8") if isinstance(s, str) else s
safe_str_cmp = lambda a, b: hmac.compare_digest(str_to_bytes(a), str_to_bytes(b))


class User(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('login', type=str, required=True, help="The field 'nome' cannot left blank.")
    argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot left blank.")
    
    #/ususarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404 #not found

    #tem que estar logado para executar
    @jwt_required()
    def delete(self, user_id):
        user_encontrado = UserModel.find_user(user_id)
        if user_encontrado:
            try:
                user_encontrado.delete_user()
            except:
                return {'message': 'An error ocurred trying to delete user.'}, 500 #Internal server error
            return {'message': 'User deletado.'}
        return {'message': 'User não encontrado.'}
        
class UserRegister(Resource):
    #/cadastro
    def post(self):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
        argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")
        dados = argumentos.parse_args()
        
        if UserModel.find_by_login(dados['login']):
            return {"message": "The login '{}' already exsists.".format(dados['login'])}
        
        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfully!'}, 201 #Criado

class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = User.argumentos.parse_args()
        #Encontrar o usuario
        user = UserModel.find_by_login(dados['login'])
        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200 #ok
        return {'message': 'The username or passwork is invalid.'}, 401 #Unauthorized