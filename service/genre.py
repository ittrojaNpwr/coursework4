from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao


    def get_one(self, gid):
        """Получение по айди"""
        return self.dao.get_one(gid)

    def get_all(self, filters):
        """Получение всех"""
        return self.dao.get_all(filters)