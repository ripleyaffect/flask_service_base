from flask_restful import Api

from .things import ThingCollectionResource


# Create the api object
api = Api(prefix='/api')


# Register resources on api endpoints
api.add_resource(ThingCollectionResource, '/things')
