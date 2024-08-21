import os
from flask import current_app, flash, render_template, request
from . import main
from .forms import UploadFileForm
from .functions import esp_get_info
from werkzeug.utils import secure_filename


def is_file_allowed(filename: str, allowed_extensions: list[str]) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


@main.route("/", methods=['GET', 'POST'])
def index():
    form = UploadFileForm()

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file found', 'error')

            return render_template('index.html', form=form, esp="")

        # check if file exists and has allowed extension
        file = request.files['file']
        allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']

        if not file or not is_file_allowed(file.filename, allowed_extensions):
            msg_invalid_file = 'Invalid file type (allowed: '\
                 + ', '.join(allowed_extensions) + ')'
            flash(msg_invalid_file, 'error')

            return render_template('index.html', form=form, esp="")

        # everything ok, get esp info from file
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        esp_info = esp_get_info(filepath)

        return render_template('index.html', form=form, esp=esp_info)

    return render_template('index.html', form=form, esp="")
