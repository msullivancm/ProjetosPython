from fastapi import FastAPI
from resources.hotel import *
from resources.site import *
from resources.usuario import *
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from resources.site import *
from models.site import *

app = FastAPI()

SQLALCHEMY_DATABASE_URI = 'sqlite:///banco.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

@app.get('/sites')
def sites():
    return {'sites': 'TESTE' } 

#Iniciar servidor: uvicorn appFastApi:app --reload