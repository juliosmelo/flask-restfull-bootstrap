# tests unitarios
import os
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src import app
from src import db
from src.models.geolocalizacao import Geolocalizacao


class GeolocalizacaoModelTestCase(unittest.TestCase): 
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(os.getenv('APP_CONFIG'))
        self.db = SQLAlchemy(self.app)
        self.db.init_app(self.app)
        with app.app_context():
            self.db.create_all()
    
    def tearDown(self):
        """
            Deletar dados
        """
        self.app = Flask(__name__)
        self.app.config.from_object(os.getenv('APP_CONFIG'))
        with self.app.app_context():
            self.db.drop_all()


    def test_salvar_localizacao(self):
        geolocalizacao = Geolocalizacao('-8.5845241', '-35.3850208')
        db.session.add(geolocalizacao)
        db.session.commit()
        self.assertEqual(geolocalizacao.latitude, '-8.5845241')
        self.assertEqual(geolocgeolocalizacaoalizao.longitude, '-35.3850208')

if __name__ == '__main__':
    unittest.main()

