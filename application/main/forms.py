from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Regexp
from application import db

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    image = FileField("Image", validators=[DataRequired()]) 
    video_url = URLField("Video URL", validators=[Length(100)])
    keyword = StringField("Keyword",validators=[Length(50)])
    submit = SubmitField("Post")

