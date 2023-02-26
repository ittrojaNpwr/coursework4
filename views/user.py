from flask_restx import Namespace, Resource
from flask import request
from dao.model.user import UserSchema
from implemented import user_service
from helpers.decorators import auth_required

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    def get(self, email):
        """Возвращает инфу по пользователю если пройдена авторизация"""
        user = user_service.get_by_email(email)
        result = UserSchema().dump(user)
        return result, 200

    @auth_required
    def patch(self, email):
        """Обновляет инфу о пользователе всё кроме пароля: имя, фамилию, любимый жанр"""
        req_json = request.json
        req_json['email'] = email
        user_service.update(req_json)
        return "", 204


@user_ns.route('/password/')
class UserPasswordView(Resource):
    @auth_required
    def put(self, email):
        """Обновляет старый пароль пользователя на новый"""
        data = request.json
        data['email'] = email
        user_service.update_password(data)
        return "", 204
