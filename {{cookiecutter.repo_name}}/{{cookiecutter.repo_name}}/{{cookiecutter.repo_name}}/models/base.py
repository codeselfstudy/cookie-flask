import datetime
import mongoengine as me

# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class Comment(me.EmbeddedDocument):
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    body = me.StringField(verbose_name="Comment", required=True)

class ContentNode(me.Document):
    """Base class for all content types. It isn't used directly, but is subclassed."""
    title = me.StringField(max_length=120, required=True)
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    content = me.StringField(required=True)
    published = me.BooleanField(required=True)
    comments = me.ListField(me.EmbeddedDocumentField('Comment'))
    comments_allowed = me.BooleanField(default=False, required=True)

    meta = {'allow_inheritance': True}
