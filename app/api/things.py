from flask_restful import Resource

from ..database.models import Thing


class ThingCollectionResource(Resource):
    def get(self):
        return { 'things': Thing.query.all() }
