from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service
from parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """Возвращает всех режиссеров, если параметр page указан, то возвращает по страницам"""
        filters = page_parser.parse_args()
        rs = director_service.get_all(filters)
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        """Возвращает фильмы по id директора"""
        r = director_service.get_one(did)
        schema_d = DirectorSchema().dump(r)
        return schema_d, 200
