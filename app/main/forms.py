"""
Form for handling file uploads using Flask-WTF.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[
        FileRequired()])
    submit = SubmitField("Submit")
