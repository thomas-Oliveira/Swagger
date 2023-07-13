from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, 
	version='1.0',
	title='Sample Swager flask code',
	description='Sample Swager flask code',
	doc="/"
	) #definição de pagina para aplicação swager

person = api.model('Person',{
			'id': fields.String(required=True, description='O Id do registro'),
			'name': fields.String(required=True, min_lenght=1, max_length=200, description='Persons name'),
			'age': fields.String(required=True, description='Person age')
			}
		) #modelo de response para ser adicionado em cada endpoint


@api.route('/') #tratamento de endpoint ( endpoint / não responde)
class Home(Resource): #a funções devem ser definidas com class e não def, com metodos de GET e POST
	def get(self,):
		return {'msn' : 'home'}

@api.route('/person')
class Person(Resource):
	@api.marshal_list_with(person) #descrição de response para cada endpoint
	def get(self,):
		return {'id': 1, "name": 'João', "age": "25"}


if __name__ == "__main__":
  app.run(debug=True)																																			


