import os
from flask import current_app, render_template, request, abort
from . import main
from .forms import UploadFileForm
from .functions import esp_get_info
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = ['bin']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route("/", methods=['GET', 'POST'])
def index():
    form = UploadFileForm()
    output = ""

    if request.method == 'POST':
        if 'file' not in request.files:
            abort(400)

        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'],
                                     filename)
            file.save(file_path)
            output = esp_get_info(file_path)
        else:
            output = "Invalid file (allowed: " + ', '.join(ALLOWED_EXTENSIONS)\
                + ")"

    return render_template('index.html', form=form, output=output)
