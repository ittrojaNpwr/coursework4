from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao


    def get_one(self, mid):
        """Получение одного по айди"""
        return self.dao.get_one(mid)

    def get_all(self, filters):
        """Получение всех"""
        return self.dao.get_all(filters)