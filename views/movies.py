from flask_restx import Namespace, Resource
from dao.model.movie import MovieSchema
from implemented import movie_service
from parsers import page_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        """Возвращает все фильмы, если указан параметр page, возвращает по страницам"""
        filters = page_parser.parse_args()
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


movie_ns.route('/<int:mid>')


class MovieView(Resource):
    def get(self, mid):
        """Возвращает фильмы по их айди"""
        b = movie_service.get_one(mid)
        schema_m = MovieSchema().dump(b)
        return schema_m, 00
