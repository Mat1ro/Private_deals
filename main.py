from flask import Flask
from flask_restx import Api

from api.config import Config
from api.setup_db import db

from students import RenderTemplateView
from api.views.fathers import father_ns
from api.views.mothers import mother_ns
from api.views.students import student_ns

api = Api(doc='/docs', prefix='/api')


def create_app(config_object):
    """create api"""
    app = Flask(__name__, template_folder='templates')
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


#     create_data(api, db)
#
#
# def create_data(api, db):
#     """create data for tables"""
#     with api.app_context():
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
app.add_url_rule(rule='/students/', view_func=RenderTemplateView.as_view(
    'about_page', template_name='index.html'))

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='localhost', port=10001)
