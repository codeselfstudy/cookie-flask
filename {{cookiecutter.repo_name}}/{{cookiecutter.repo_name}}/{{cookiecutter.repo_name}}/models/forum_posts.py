import mongoengine as me
from .base import ContentNode


# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class ForumPost(ContentNode):
    category = me.StringField()
    comments_allowed = me.BooleanField(default=True, required=True)
