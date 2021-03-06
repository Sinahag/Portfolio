from application import db
from datetime import datetime

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

# TODO: Build out the Post Model to enable image upload and make blog posts
# referemce: https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples/quickimages
class Post(Blog):
    __tablename__ = "posts"
    title = db.StringField(max_length=200, nullable=False)
    description = db.StringField(max_length=1000)
    image = db.ImageField(size=(300, 300, True), thumbnail_size=(30, 30, True))
    keyword = db.StringField(max_length=50)