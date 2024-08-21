import os
from flask import current_app, flash, render_template, request, redirect, \
    url_for
from . import main
from .forms import UploadFileForm
from .functions import esp_get_info
from werkzeug.utils import secure_filename


def is_file_allowed(filename: str, allowed_extensions: list[str]) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


@main.errorhandler(413)
def file_too_large(e):
    max_file_size = current_app.config['MAX_CONTENT_LENGTH'] / 1000 / 1000
    msg_too_large = 'File is too large (max: ' + str(max_file_size) + 'MB)!'
    flash(msg_too_large, 'error')
    return redirect(url_for('main.index'))


@main.route("/", methods=['GET', 'POST'])
def index():
    form = UploadFileForm()

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file found', 'error')

            return redirect(url_for('main.index'))

        # check if file exists and has allowed extension
        file = request.files['file']
        allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']

        if not file or not is_file_allowed(file.filename, allowed_extensions):
            msg_invalid_file = 'Invalid file type (allowed: '\
                 + ', '.join(allowed_extensions) + ')!'
            flash(msg_invalid_file, 'error')

            return redirect(url_for('main.index'))

        # everything ok, get esp info from file
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        esp_info = esp_get_info(filepath)

        success_msg = "File " + str(filename) + " successfully analyzed!"
        flash(success_msg, 'success')

        return render_template('index.html', form=form, esp=esp_info)

    return render_template('index.html', form=form)
