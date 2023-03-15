from marshmallow import Schema, fields
from api.setup_db import db


class Father(db.Model):
    """Create table for father"""
    __tablename__ = 'father'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    surname = db.Column(db.String, nullable=True)
    patronymic = db.Column(db.String, nullable=True)
    number = db.Column(db.String, nullable=True)
    job = db.Column(db.String, nullable=True)


class FatherSchema(Schema):
    """Create schema for father"""
    id = fields.Integer()
    name = fields.String()
    surname = fields.String()
    patronymic = fields.String()
    number = fields.String()
    job = fields.String()
