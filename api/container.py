from api.setup_db import db

from dao import FatherDAO
from service import FatherService
from dao import MotherDAO
from service.mother import MotherService
from dao import StudentDAO
from service.student import StudentService

father_dao = FatherDAO(db.session)
father_service = FatherService(father_dao)

mother_dao = MotherDAO(db.session)
mother_service = MotherService(mother_dao)

student_dao = StudentDAO(db.session)
student_service = StudentService(student_dao)
