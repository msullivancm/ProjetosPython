from flask_restful import Resource, reqparse
from models.hotel import *
from flask_jwt_extended import jwt_required
from flask import request

#normalizar path para passagem de parâmetros corretamente
def normaliza_path_params(cidade=None,
                          estrelas_min = 0,
                          estrelas_max = 5,
                          diaria_min = 0,
                          diaria_max = 10000,
                          limit = 50,
                          offset = 0, **dados):
    if cidade: 
        return {
            'estrelas_min': estrelas_min, 
            'estrelas_max': estrelas_max, 
            'diaria_min': diaria_min, 
            'diaria_max': diaria_max, 
            'cidade': cidade, 
            'limit': limit, 
            'offset': offset
        } #se existir cidade retorna tudo
    return {
            'estrelas_min': estrelas_min, 
            'estrelas_max': estrelas_max, 
            'diaria_min': diaria_min, 
            'diaria_max': diaria_max, 
            'limit': limit, 
            'offset': offset
        } #se não existir cidade retorna tudo menos cidade

#implementação de passagem de parametro pelo path
#path /hoteis?cidade=Rio de Janeiro&estrelas_min=4&estrelas_max=5&diaria_min=100&diaria_max=400&limit=10&offset=0
path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float) #paginação
path_params.add_argument('offset', type=float) #quantidade de elementos que desejamos pular, complemento da paginação

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()] }
    
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot left blank.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot left blank.")
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
        
    #esta é uma função da classe, por isso não passa o self. 
    # Se passasse o self procuraria só no registro atual e não no conjunto de registros da classe.
    
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 #not found
    
    #tem que estar logado para executar
    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400 # bad request
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel() #salva o hotel no banco de dados
        except:
            return {'message': 'Internal error trying to save hotel.'}, 500 #Internal server error
        return hotel.json(), 200 #Sucesso

    #tem que estar logado para executar
    @jwt_required()
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado: 
            hotel_encontrado.update_hotel(**dados) #utiliza os dados recebidos como argumento para atualizar o registro
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200 #ok atualizado
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel() #salva o hotel no banco de dados
        except:
            return {'message': 'Internal error trying to save hotel.'}, 500 #Internal server error
        return hotel.json(), 201 #criado

    #tem que estar logado para executar
    @jwt_required()
    def delete(self, hotel_id):
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            try:
                hotel_encontrado.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel.'}, 500 #Internal server error
            return {'message': 'Hotel deletado.'}
        return {'message': 'Hotel não encontrado.'}
        