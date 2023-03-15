from app.container import father_service
from app.dao.model.father import FatherSchema

from flask_restx import Namespace, Resource
from flask import request

father_ns = Namespace("fathers")

father_schema = FatherSchema()
fathers_schema = FatherSchema(many=True)


@father_ns.route("/")
class FathersView(Resource):
    """
    the link "/fathers/" has GET, POST requests
    """

    def get(self):
        """
        :return: dictionary list with data on all fathers
        """
        return fathers_schema.dump(father_service.get_all()), 200

    def post(self):
        """
        :return: code 204, if a new entry in the DB was successfully made
        """
        data = request.json
        father_service.create(data)
        return "", 201


@father_ns.route("/<int:fid>")
class FatherView(Resource):

    def get(self, fid):
        """
        :param fid: father's id
        :return: dictionary with data about one father by his identifier
        """
        return father_schema.dump(father_service.get_one(fid)), 200

    def put(self, fid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        father_service.update(data, fid)
        return "", 204

    def patch(self, fid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        father_service.update_partial(data, fid)
        return "", 204

    def delete(self, fid):
        """
        :param fid: father's id
        :return: code 204, if the new record in the database was successfully delete
        """
        return father_service.delete(fid), 204
