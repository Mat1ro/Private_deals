from flask.views import View
from flask import request, render_template

from api.container import student_service
from api.views.students import students_schema


class StudentsView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, data):
        return render_template(self.get_template_name(), **data)

    def dispatch_request(self):
        students = students_schema.dump(student_service.get_all()), 200
        return self.render_template(students)


class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)
