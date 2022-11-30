from flask_restful import Resource, reqparse
from models.usuarios import *
    
class User(Resource):
    #/ususarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404 #not found
    
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
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
        atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")
        dados = atributos.parse_args()
        
        if UserModel.find_by_login(dados['login']):
            return {"message": "The login '{}' already exsists.".format(dados['login'])}
        
        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfully!'}, 201 #Criado
        