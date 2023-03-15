from app.setup_db import db

from app.dao.father import FatherDAO
from app.service.father import FatherService
from app.dao.mother import MotherDAO
from app.service.mother import MotherService
from app.dao.student import StudentDAO
from app.service.student import StudentService

father_dao = FatherDAO(db.session)
father_service = FatherService(father_dao)

mother_dao = MotherDAO(db.session)
mother_service = MotherService(mother_dao)

student_dao = StudentDAO(db.session)
student_service = StudentService(student_dao)
