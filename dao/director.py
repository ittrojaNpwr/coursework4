from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        """Получение одного директора по его ID"""
        return self.session.query(Director).get(did)

    def get_all(self, filters):
        """Получение всех директоров! и их пагинация"""
        page = filters.get('page')
        directors = self.session.query(Director)
        return directors.paginate(page=page, per_page=12).items
