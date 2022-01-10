from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length
from application import db


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    image = FileField("Image", validators=[DataRequired()]) 
    keyword = StringField("Keyword",validators=[Length(50)])
    submit = SubmitField("Post")
