from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_admin import Admin
from .views.admin import AdminIndexView
import mongoengine as me
from flask_pagedown import PageDown
from flask.ext.misaka import Misaka


# Import routes and logic for each section of the website from the views directory
# Prevent circular imports
def register_blueprints(app_instance):
    from .views.pages import pages_bp
    from .views.forum import forum_bp
    app_instance.register_blueprint(pages_bp)
    app_instance.register_blueprint(forum_bp)

app = Flask(__name__, instance_relative_config=True)

# From default to overridden
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
# Need to set APP_CONFIG_FILE to use this option
# app.config.from_envvar('APP_CONFIG_FILE')

# TODO: move app.debug out of here.
app.debug = True

# Debug toolbar must come after app.debug = True
toolbar = DebugToolbarExtension(app)

# Admin dashboard
admin = Admin(app, name='Admin Panel')
admin.add_view(AdminIndexView(name='Content', endpoint='someplace'))
admin.add_view(AdminIndexView(name='Page I', endpoint='page1', category='Content Moderation'))
admin.add_view(AdminIndexView(name='Page II', endpoint='page2', category='Content Moderation'))
admin.add_view(AdminIndexView(name='Page III', endpoint='page3', category='Content Moderation'))

# Database
me.connect(app.config['MONGODB_DB'])

# Markdown frontend
pagedown = PageDown(app)
# Markdown backend
Misaka(app)

register_blueprints(app)
