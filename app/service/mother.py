from app.dao.mother import MotherDAO


class MotherService:

    def __init__(self, dao: MotherDAO):
        self.dao = dao

    def get_all(self):
        """
        :return: mother DAO get_all() method
        """
        return self.dao.get_all()

    def get_one(self, mid):
        """
        :param mid: mother's Id
        :return:  mother DAO get_one() method with argument mid
        """
        return self.dao.get_one(mid)

    def create(self, data):
        """
        :param data: information about the mother to be added to the DB
        :return: mother DAO create() method, with argument data
        """
        return self.dao.create(data)

    def update(self, data, mid):
        """
        :param data: information about the mother to be added to the DB
        :return: mother DAO update() method, with argument data
        """
        mother = self.get_one(mid)

        mother.name = data["name"]
        mother.surname = data["surname"]
        mother.patronymic = data["patronymic"]
        mother.number = data["number"]
        mother.job = data["job"]

        return self.dao.update(mother)

    def update_partial(self, data, mid):
        """
        :param data: information about the mother to be added to the DB
        :return: mother DAO update() method, with argument data
        """

        mother = self.get_one(mid)

        if "name" in data:
            mother.name = data["name"]
        if "surname" in data:
            mother.surname = data["surname"]
        if "patronymic" in data:
            mother.patronymic = data["patronymic"]
        if "number" in data:
            mother.number = data["number"]
        if "job" in data:
            mother.job = data["job"]
        print()

        return self.dao.update(mother)

    def delete(self, mid):
        """
        :param mid: mother's Id
        :return: mother DAO delete()
        """
        return self.dao.delete(mid)

    def get_by_name_and_surname(self, name, surname):
        """
        :param name: mother's name
        :param surname: mother's surname
        :return: mother DAO get_by_name_and_surname(), with argument name and surname
        """
        return self.dao.get_by_name_and_surname(name, surname)