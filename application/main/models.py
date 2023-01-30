from application import db
from datetime import datetime
from flask import flash
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
        x = re.search("^(http(|s):\/\/)*(www.)*github.com\/(S|s)inahag", url)
        if not x and len(url)>0:
            flash("invalid github url", "warning")
            raise ValueError()

    def check_valid_video_url(url):
        x = re.search("^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)*?", url)
        if not x and len(url)>0:
            flash("invalid youtube url", "warning")
            raise ValueError()

    def check_valid_title(title):
        title_exists = Post.objects(title=title).first()
        if title_exists:
            flash('A Post Exists with this Title', "warning")
            raise ValueError()
        elif  len(title)<5:
            flash('A title must exceed 5 characters', "error")
            raise ValueError()

    def check_valid_description(description):
        if not len(description):
            flash('A post description is mandatory', "error")
            raise ValueError()

    __tablename__ = "posts"
    title = db.StringField(max_length=200, nullable=False, validation=check_valid_title)
    description = db.StringField(max_length=1000,validation=check_valid_description)
    video_url = db.StringField(max_length=100, validation=check_valid_video_url)
    github_url = db.StringField(max_length=200, validation=check_valid_github_url)
    image = db.ImageField(size=(500, 500, False), thumbnail_size=(60, 60, False))
    keyword = db.StringField(max_length=50)
    user = db.StringField(max_length=100)

