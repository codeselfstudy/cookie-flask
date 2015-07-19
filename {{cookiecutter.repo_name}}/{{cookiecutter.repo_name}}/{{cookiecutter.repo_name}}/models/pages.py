import mongoengine as me
from .base import ContentNode


class Page(ContentNode):
    slug = me.StringField(max_length=120, required=True)
