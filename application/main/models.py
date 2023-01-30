from application import db
from datetime import datetime
import re


class Blog(db.Document):
    __abstract__ = True
    meta = {'allow_inheritance': True}
    id = db.IntField(primary_key=True, autoincrement=True)
    date_created = db.DateTimeField(nullable=False, default=datetime.utcnow)
    date_modified = db.DateTimeField(nullable=False, default=datetime.utcnow,
                              onupdate=lambda: datetime.utcnow())

    def to_dict(self):
        return {'id': self.id,
                'date_created': self.date_created,
                'date_modified': self.date_modified}

# referemce: https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples/quickimages
class Post(Blog):
    def check_valid_github_url(url):
        x = re.search("^\b(https:\/\/)*www.github.com\/(sinahag)\b\/", url)
        if x:
            raise ValidationError("invalid github url")

    def check_valid_video_url(url):
        x = re.search("^http\b(s:\/\/)*(www.)*(youtube)*\b", url)
        if x:
            raise ValidationError("invalid youtube url")

    __tablename__ = "posts"
    title = db.StringField(max_length=200, nullable=False)
    description = db.StringField(max_length=1000)
    video_url = db.StringField(max_length=100)
    github_url = db.StringField(max_length=200)
    image = db.ImageField(size=(500, 500, False), thumbnail_size=(60, 60, False))
    keyword = db.StringField(max_length=50)
    user = db.StringField(max_length=100)

