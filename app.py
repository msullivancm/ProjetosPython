from flask import Flask
from flask_restful import Api
from resources.hotel import *
from resources.usuario import *

app = Flask(__name__)
#Define o banco de dados que será criado, independente do driver de banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
#não é necessário rastrear as modificações porque o flask já faz isso
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

#Antes de fazer a primeira conexão cria o banco de dados
@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')

if __name__ == '__main__':
    #Chama o sql_alchemy e inicializa o banco de dados antes de iniciar o app
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)