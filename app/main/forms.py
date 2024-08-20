from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

ALLOWED_EXTENSIONS = ['bin']


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[
        FileRequired(),
        FileAllowed(ALLOWED_EXTENSIONS, "extension not allowed!")])
    submit = SubmitField('Submit')
