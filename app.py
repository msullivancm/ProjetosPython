from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import *
from resources.site import *
from resources.usuario import *
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
#Define o banco de dados que será criado, independente do driver de banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
#não é necessário rastrear as modificações porque o flask já faz isso
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLE'] = True
api = Api(app)
jwt = JWTManager(app)

#Antes de fazer a primeira conexão cria o banco de dados
@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verificar_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401 #Unauthorized

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Sites, '/sites')
api.add_resource(Site, '/site/<string:url>')

if __name__ == '__main__':
    #Chama o sql_alchemy e inicializa o banco de dados antes de iniciar o app
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)