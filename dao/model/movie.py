from marshmallow import Schema, fields
from setup_db import db
from dao.model.genre import Genre
from dao.model.director import Director


class Movie(db.Model):
    """Создание таблички Movie для БД"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    year = fields.Str()
    rating = fields.Float()