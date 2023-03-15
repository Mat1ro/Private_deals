from app.dao.student import StudentDAO


class StudentService:

    def __init__(self, dao: StudentDAO):
        self.dao = dao

    def get_all(self):
        """
        :return: student DAO get_all() method
        """
        return self.dao.get_all()

    def get_one(self, fid):
        """
        :param fid: student's Id
        :return:  student DAO get_one() method with argument fid
        """
        return self.dao.get_one(fid)

    def create(self, data):
        """
        :param data: information about the student to be added to the DB
        :return: student DAO create() method, with argument data
        """
        return self.dao.create(data)

    def update(self, data, fid):
        """
        :param data: information about the student to be added to the DB
        :return: student DAO update() method, with argument data
        """
        student = self.get_one(fid)

        student.name = data["name"]
        student.surname = data["surname"]
        student.patronymic = data["patronymic"]
        student.number = data["number"]
        student.job = data["job"]

        return self.dao.update(student)

    def update_partial(self, data, fid):
        """
        :param data: information about the student to be added to the DB
        :return: student DAO update() method, with argument data
        """

        student = self.get_one(fid)

        if "name" in data:
            student.name = data["name"]
        if "surname" in data:
            student.surname = data["surname"]
        if "patronymic" in data:
            student.patronymic = data["patronymic"]
        if "number" in data:
            student.number = data["number"]
        if "job" in data:
            student.job = data["job"]
        print()

        return self.dao.update(student)

    def delete(self, fid):
        """
        :param fid: student's Id
        :return: student DAO delete()
        """
        return self.dao.delete(fid)

    def get_by_name_and_surname(self, name, surname):
        """
        :param name: student's name
        :param surname: student's surname
        :return: student DAO get_by_name_and_surname(), with argument name and surname
        """
        return self.dao.get_by_name_and_surname(name, surname)