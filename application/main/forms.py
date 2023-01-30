from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from application import db

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    image = FileField("Image", validators=[DataRequired()]) 
    video_url = StringField("Video URL",  validators=[Regexp('^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)*?')])
    github_url = StringField("GitHub", validators=[Regexp('^(http(|s):\/\/)*(www.)*github.com\/(S|s)inahag')])
    keyword = StringField("Keyword",validators=[Length(max=50)])
    submit = SubmitField("Post")