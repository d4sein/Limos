from flask import request
from flask_restful import Resource

from app import app
from app.models import Food, FoodSchema


class Index(Resource):
    def get(self):
        param = request.args.to_dict()

        if set(param) == {'search'}:
            key = param['search']
            query = Food.query.filter(Food.description.like(f'%{key}%')).all()
            
            result = [food.description for food in query]
        
        elif set(param) == {'food'}:
            key = param['food']
            food = Food.query.filter_by(description=key).first()

            result = FoodSchema().dump(food)

        else:
            return {'error': 'Couldn\'t find the right params'}, 400

        if not result:
            return {}, 204

        return {'food': result}, 200


app.api.add_resource(Index, '/')
