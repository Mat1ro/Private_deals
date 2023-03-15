from dao.model.mother import Mother


class MotherDAO:

    def __init__(self, session):
        """
        :param session: db.session
        """
        self.session = session

    def get_all(self):
        """
        :return: list with all instances of the Mother class:
        """
        return self.session.query(Mother).all()

    def get_one(self, fid):
        """
        :param fid: mother's id
        :return:  one instance of the Mother class by id
        """
        return self.session.query(Mother).get(fid)

    def create(self, data):
        """
        :param data: dictionary with data to create a new record in the table Mothers
        :return: one new instance of the class
        """
        mother = Mother(**data)

        self.session.add(mother)
        self.session.commit()

        return mother

    def update(self, mother):
        """
        :param mother: a bulked-up instance of the Mother class
        :return: a bulked-up instance of the mother class
        """
        self.session.add(mother)
        self.session.commit()

        return mother

    def delete(self, mid):
        """
        :param mid: the id of the Mother you want to remove
        :return: None
        """
        self.session.delete(self.session.query(Mother).get(mid))
        self.session.commit()

    def get_by_name_and_surname(self, name, surname):
        """
        :param name: mother's name
        :param surname: mother's surname
        :return: instance of the Mother class
        """
        return self.session.query(Mother).filter(Mother.name == name, Mother.surname == surname).first()
