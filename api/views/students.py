from api.container import student_service
from dao import StudentSchema

from flask_restx import Namespace, Resource
from flask import request

student_ns = Namespace("students")

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


@student_ns.route("/")
class StudentsView(Resource):
    """
    the link "/students/" has GET, POST requests
    """

    def get(self):
        """
        :return: dictionary list with data on all students
        """
        return students_schema.dump(student_service.get_all()), 200

    def post(self):
        """
        :return: code 204, if a new entry in the DB was successfully made
        """
        data = request.json
        student_service.create(data)
        return '', 201


@student_ns.route("/<int:sid>")
class StudentView(Resource):

    def get(self, sid):
        """
        :param sid: student's id
        :return: dictionary with data about one student by his identifier
        """
        return student_schema.dump(student_service.get_one(sid)), 200

    def put(self, sid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        student_service.update(data, sid)
        return "", 204

    def patch(self, sid):
        """
        :return: code 204, if the new record in the database was successfully updated
        """
        data = request.json

        student_service.update_partial(data, sid)
        return "", 204

    def delete(self, sid):
        """
        :param sid: student's id
        :return: code 204, if the new record in the database was successfully delete
        """
        return student_service.delete(sid), 204
