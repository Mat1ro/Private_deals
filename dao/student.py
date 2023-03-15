from dao.model.student import Student


class StudentDAO:

    def __init__(self, session):
        """
        :param session: db.session
        """
        self.session = session

    def get_all(self):
        """
        :return: list with all instances of the Student class:
        """
        return self.session.query(Student).all()

    def get_one(self, fid):
        """
        :param fid: student's id
        :return:  one instance of the Student class by id
        """
        return self.session.query(Student).get(fid)

    def create(self, data):
        """
        :param data: dictionary with data to create a new record in the table students
        :return: one new instance of the class
        """
        student = Student(**data)

        self.session.add(student)
        self.session.commit()

        return student

    def update(self, student):
        """
        :param student: a bulked-up instance of the Student class
        :return: a bulked-up instance of the Student class
        """
        self.session.add(student)
        self.session.commit()

        return student

    def delete(self, fid):
        """
        :param fid: the id of the student you want to remove
        :return: None
        """
        self.session.delete(self.session.query(Student).get(fid))
        self.session.commit()

    def get_by_name_and_surname(self, name, surname):
        """
        :param name: student's name
        :param surname: student's surname
        :return: instance of the Student class
        """
        return self.session.query(Student).filter(Student.name == name, Student.surname == surname).first()
