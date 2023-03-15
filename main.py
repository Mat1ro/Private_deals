from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.model.father import Father
from app.dao.model.mother import Mother
from app.dao.model.student import Student
from app.setup_db import db

from app.views.fathers import father_ns
from app.views.mothers import mother_ns
from app.views.students import student_ns

api = Api(doc='/docs')


def create_app(config_object):
    """create app"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """register extensions"""
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(father_ns)
    api.add_namespace(mother_ns)
    api.add_namespace(student_ns)


#     create_data(app, db)
#
#
# def create_data(app, db):
#     """create data for tables"""
#     with app.app_context():
#         db.drop_all()
#         db.create_all()
#         f1 = Father(name='Kolya', surname='Boronov', patronymic='Leontivich', number='+79093048073', job='retired')
#         m1 = Mother(name='Nadya', surname='Boronova', patronymic='Markovna', number='+79093048072', job='akkond')
#         s1 = Student(name='Roma', surname='Boronov', patronymic='Nikolaevich', role='student', age=16, gender='male',
#                      number='+79674727177', photo='path', email='r.boronov@it-park.tech', password='cool_password',
#                      school='Singularity hub', mother_id=1, father_id=1)
#         with db.session.begin():
#             db.session.add_all([s1, f1, m1])


app = create_app(Config())

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run()
