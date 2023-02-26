from flask_restx import Namespace, Resource
from implemented import favorites_service
from helpers.decorators import auth_required

favorites_ns = Namespace('favorites/movies/')


@favorites_ns.route('/<int:mid>')
class FavoritesView(Resource):
    @auth_required
    def post(self, mid, email):
        """Создает запись в таблице фильмов-фаворитов, а именно id user, id movie"""
        favorites_service.create(mid, email)
        return "", 201

    @auth_required
    def delete(self, mid, email):
        """Удаляет зпись в тблице фильмов-фаворитов, а именно id user, id movie"""
        favorites_service.delete(mid, email)
        return "", 204
