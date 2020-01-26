from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Application:
    '''Instantiates the Application "wrapper" object'''
    def __init__(self) -> None:
        # Instantiates WSGI Application
        self.server = Flask(__name__)
        # Instantiates RESTful API
        self.api = Api(self.server)

    def set_config(self, config: str) -> None:
        '''
        Sets configs for the Application
        
        Parameters:
            config: str
            Module object where to get the configs from
        '''
        self.server.config.from_object(config)
    
    def set_database(self) -> None:
        '''Instantiates Database'''
        self.db = SQLAlchemy(self.server)
        self.ma = Marshmallow(self.server)


app = Application()
app.set_config('config')
app.set_database()

from app import controllers, models
