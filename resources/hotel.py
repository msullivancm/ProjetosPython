from flask_restful import Resource, reqparse
from models.hotel import *
from models.site import *
from flask_jwt_extended import jwt_required
from flask import request

class Hoteis(Resource):
    #implementação de passagem de parametro pelo path
    #path /hoteis?cidade=Rio de Janeiro&estrelas_min=4&estrelas_max=5&diaria_min=100&diaria_max=400&limit=10&offset=0
    query_params = reqparse.RequestParser()
    query_params.add_argument("cidade", type=str, default="", location="args")
    query_params.add_argument("estrelas_min", type=float, default=0, location="args")
    query_params.add_argument("estrelas_max", type=float, default=5, location="args")
    query_params.add_argument("diaria_min", type=float, default=0, location="args")
    query_params.add_argument("diaria_max", type=float, default=10000, location="args")
    query_params.add_argument("limit", type=float, default=10, location="args")
    query_params.add_argument("offset", type=float, default=0, location="args")
    
    def get(self):
        filters = Hoteis.query_params.parse_args()
 
        query = HotelModel.query
 
        if filters["cidade"]:
            query = query.filter(HotelModel.cidade == filters["cidade"])
        elif filters["estrelas_min"]:
            query = query.filter(HotelModel.estrelas >= filters["estrelas_min"])
        elif filters["estrelas_max"]:
            query = query.filter(HotelModel.estrelas <= filters["estrelas_max"])
        elif filters["diaria_min"]:
            query = query.filter(HotelModel.diaria >= filters["diaria_min"])
        elif filters["diaria_max"]:
            query = query.filter(HotelModel.diaria <= filters["diaria_max"])
        elif filters["limit"]:
            query = query.filter(HotelModel.diaria <= filters["limit"])
        elif filters["offset"]:
            query = query.filter(HotelModel.diaria <= filters["offset"])
        else: 
            return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()] }
 
        return {"hoteis": [hotel.json() for hotel in query]}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot left blank.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot left blank.")
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    argumentos.add_argument('site_id', type=int, required=True, help="Every hotel needs linked with site.")
        
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
        
        if not SiteModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be assossiated to site'}, 400 # bad request
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

