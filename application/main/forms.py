from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from application import db

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    image = FileField("Image", validators=[DataRequired()]) 
    video_url = StringField("Video URL",  validators=[Regexp('^http\b(s:\/\/)*(www.)*(youtube)*\b')])
    github_url = StringField("GitHub", validators=[Regexp('^\b(https:\/\/)*www.github.com\/(sinahag)\b\/')])
    keyword = StringField("Keyword",validators=[Length(50)])
    submit = SubmitField("Post")