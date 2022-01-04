from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length
from application import db


class PostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])
    image = FileField("image", validators=[DataRequired()]) 
    keyword = StringField("keyword",validators=[Length(50)])
    submit = SubmitField("Post")
