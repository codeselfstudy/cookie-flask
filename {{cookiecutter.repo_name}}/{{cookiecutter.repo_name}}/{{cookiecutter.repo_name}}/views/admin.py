from flask_admin import Admin, BaseView, expose


# TODO: Implement authentication and functionality
# https://flask-admin.readthedocs.org/en/latest/quickstart/#authentication

class AdminIndexView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


