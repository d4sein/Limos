from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Application:
    def __init__(self) -> None:
        '''Instantiates the Application "wrapper" object'''
        # Instantiates the WSGI Application object
        self.server = Flask(__name__)
        # Instantiates the Database object
        self.db = SQLAlchemy(self.server)
        # Instantiates the ODM object
        self.ma = Marshmallow(self.server)

    def set_config(self, config: str) -> None:
        '''
        Sets configs for the Application
        
        Parameters:
            config: str
            Module object where to get the configs from
        '''
        # Sets the config for App
        self.server.config.from_object(config)
        # Creates the database
        self.db.create_all()
    

app = Application()
app.set_config('config')
