from dao.model.father import Father


class FatherDAO:

    def __init__(self, session):
        """
        :param session: db.session
        """
        self.session = session

    def get_all(self):
        """
        :return: list with all instances of the Father class:
        """
        return self.session.query(Father).all()

    def get_one(self, fid):
        """
        :param fid: father's id
        :return:  one instance of the Father class by id
        """
        return self.session.query(Father).get(fid)

    def create(self, data):
        """
        :param data: dictionary with data to create a new record in the table fathers
        :return: one new instance of the class
        """
        father = Father(**data)

        self.session.add(father)
        self.session.commit()

        return father

    def update(self, father):
        """
        :param father: a bulked-up instance of the Father class
        :return: a bulked-up instance of the Father class
        """
        self.session.add(father)
        self.session.commit()

        return father

    def delete(self, fid):
        """
        :param fid: the id of the father you want to remove
        :return: None
        """
        self.session.delete(self.session.query(Father).get(fid))
        self.session.commit()

    def get_by_name_and_surname(self, name, surname):
        """
        :param name: father's name
        :param surname: father's surname
        :return: instance of the Father class
        """
        return self.session.query(Father).filter(Father.name == name, Father.surname == surname).first()
