import base64
import hashlib
import hmac

from flask_restx import abort

from dao.user import UserDAO
from helpers.constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        """Получение по айди"""
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        """Получение по емаил"""
        return self.dao.get_by_email(email)

    def create(self, data):
        """Создание пользователя"""
        return self.dao.create(data)

    def update(self, data):
        """Апгрейд"""
        return self.dao.update(data)

    def get_hash(self, password):
        """Принимает пароль и отдает его хэш"""
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS,
        ))

    def compare_passwords(self, password_hash, password):
        """Принимает хэш пароль и введеный пароль, хэширует введенный, делает сравнение и возвращает True или False"""
        new_hash = base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS,
        ))
        return hmac.compare_digest(password_hash, new_hash)

    def update_password(self, data):
        """Принимает старый и новый пароль, проверяет старый на совпадение и если совпадает, осуществляет обновление пароля на новый"""

        user = self.get_by_email(data.get('email'))
        if user is None:
            raise abort(404)
        if not self.compare_passwords(user.password, data.get('passoword_1')):
            abort(400)

        data["password_2"] = self.get_hash(data.get('password_2'))
        self.dao.update_password(data)
