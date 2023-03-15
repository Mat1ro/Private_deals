from marshmallow import Schema, fields
from sqlalchemy.orm import relationship
from app.setup_db import db


class Student(db.Model):
    """Create table for student"""
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    surname = db.Column(db.String, nullable=True)
    patronymic = db.Column(db.String, nullable=True)
    role = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String)
    number = db.Column(db.String, nullable=True)
    photo = db.Column(db.String)
    email = db.Column(db.String, nullable=True, unique=True)
    password = db.Column(db.String, nullable=True)
    school = db.Column(db.String, nullable=True)

    mother_id = db.Column(db.Integer, db.ForeignKey("mother.id"))
    mother = relationship("Mother")
    father_id = db.Column(db.Integer, db.ForeignKey("father.id"))
    father = relationship("Father")


class StudentSchema(Schema):
    """Create schema for student"""
    id = fields.Integer()
    name = fields.String()
    surname = fields.String()
    patronymic = fields.String()
    role = fields.String()
    age = fields.Integer()
    gender = fields.String()
    number = fields.String()
    photo = fields.String()
    email = fields.String()
    password = fields.String()
    school = fields.String()
    mother_id = fields.Integer()
    father_id = fields.Integer()
