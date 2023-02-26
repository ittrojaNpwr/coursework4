from dao.director import DirectorDAO

class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        """Получение по айди"""
        return self.dao.get_one(did)

    def get_all(self, filters):
        """Получение всех"""
        return self.dao.get_all(filters)