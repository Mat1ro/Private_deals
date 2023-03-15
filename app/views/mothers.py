from app.container import mother_service
from app.dao.model.mother import MotherSchema

from flask_restx import Namespace, Resource
from flask import request


mother_ns = Namespace("mothers")

mother_schema = MotherSchema()
mothers_schema = MotherSchema(many=True)

@mother_ns.route("/")
class MothersView(Resource):
    """
    the link "/mothers/" has GET, POST requests
    """
    def get(self):
        """
        :return: dictionary list with data on all mothers
        """
        return mothers_schema.dump(mother_service.get_all()), 200

    def post(self):
        """
        :return: code 204, if a new entry in the DB was successfully made
        """
        data = request.json
        mother_service.create(data)
        return "", 201


@mother_ns.route("/<int:mid>")
class MotherView(Resource):

    def get(self, mid):
        """
        :param fid: mother's id
        :return: dictionary with data about one mother by his identifier
        """
        return mother_schema.dump(mother_service.get_one(mid)), 200

    def put(self, mid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        mother_service.update(data, mid)
        return "", 204

    def patch(self, mid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        mother_service.update_partial(data, mid)
        return "", 204

    def delete(self, mid):
        """
        :param mid: mother's id
        :return: code 204, if the new record in the database was successfully delete
        """
        return mother_service.delete(mid), 204