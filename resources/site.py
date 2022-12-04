from flask_restful import Resource, reqparse
from models.site import *
from flask_jwt_extended import jwt_required
from flask import request

class Sites(Resource):
    query_params = reqparse.RequestParser()
    query_params.add_argument("url", type=str, default="", location="args")
    
    def get(self):
        return {'sites': [site.json() for site in SiteModel.query.all()] }
 
class Site(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('url', type=str, required=True, help="The field 'url' cannot left blank.")
        
    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {'message': 'Site not found.'}, 404 #not found
    
    #tem que estar logado para executar
    @jwt_required()
    def post(self, url):
        if SiteModel.find_site(url):
            return {"message": "Site id '{}' already exists.".format(url)}, 400 # bad request
        site = SiteModel(url)
        try:
            site.save_site() #salva
        except:
            return {'message': 'Internal error trying to save site.'}, 500 #Internal server error
        return site.json(), 200 #Sucesso

    #tem que estar logado para executar
    @jwt_required()
    def put(self, url):
        dados = Site.argumentos.parse_args()
        
        site_encontrado = SiteModel.find_site(url)
        if site_encontrado: 
            site_encontrado.update_site(**dados) #utiliza os dados recebidos como argumento para atualizar o registro
            site_encontrado.save_site()
            return site_encontrado.json(), 200 #ok atualizado
        site = SiteModel(url, **dados)
        try:
            site.save_hotel() #salva o hotel no banco de dados
        except:
            return {'message': 'Internal error trying to save site.'}, 500 #Internal server error
        return site.json(), 201 #criado

    #tem que estar logado para executar
    @jwt_required()
    def delete(self, url):
        site_encontrado = SiteModel.find_site(url)
        if site_encontrado:
            try:
                site_encontrado.delete_site()
            except:
                return {'message': 'An error ocurred trying to delete site.'}, 500 #Internal server error
            return {'message': 'Site deletado.'}
        return {'message': 'Site não encontrado.'}

