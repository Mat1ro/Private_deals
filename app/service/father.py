from app.dao.father import FatherDAO


class FatherService:

    def __init__(self, dao: FatherDAO):
        self.dao = dao

    def get_all(self):
        """
        :return: father DAO get_all() method
        """
        return self.dao.get_all()

    def get_one(self, fid):
        """
        :param fid: father's Id
        :return:  father DAO get_one() method with argument fid
        """
        return self.dao.get_one(fid)

    def create(self, data):
        """
        :param data: information about the father to be added to the DB
        :return: father DAO create() method, with argument data
        """
        return self.dao.create(data)

    def update(self, data, fid):
        """
        :param data: information about the father to be added to the DB
        :return: father DAO update() method, with argument data
        """
        father = self.get_one(fid)

        father.name = data["name"]
        father.surname = data["surname"]
        father.patronymic = data["patronymic"]
        father.number = data["number"]
        father.job = data["job"]

        return self.dao.update(father)

    def update_partial(self, data, fid):
        """
        :param data: information about the father to be added to the DB
        :return: father DAO update() method, with argument data
        """

        father = self.get_one(fid)

        if "name" in data:
            father.name = data["name"]
        if "surname" in data:
            father.surname = data["surname"]
        if "patronymic" in data:
            father.patronymic = data["patronymic"]
        if "number" in data:
            father.number = data["number"]
        if "job" in data:
            father.job = data["job"]
        print()

        return self.dao.update(father)

    def delete(self, fid):
        """
        :param fid: father's Id
        :return: father DAO delete()
        """
        return self.dao.delete(fid)

    def get_by_name_and_surname(self, name, surname):
        """
        :param name: father's name
        :param surname: father's surname
        :return: father DAO get_by_name_and_surname(), with argument name and surname
        """
        return self.dao.get_by_name_and_surname(name, surname)
