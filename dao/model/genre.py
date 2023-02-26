from marshmallow import Schema, fields
from setup_db import db

class Genre(db.Model):
    """Создание таблички Genre для БД"""
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()