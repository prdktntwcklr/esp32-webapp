import os
from flask import current_app, render_template, request
from . import main
from .forms import UploadFileForm
from .functions import esp_get_info
from werkzeug.utils import secure_filename


@main.route("/", methods=['GET', 'POST'])
def index():
    form = UploadFileForm()
    output = ""

    if request.method == 'POST':
        if form.validate_on_submit():
            file = form.file.data

            if file:
                filename = secure_filename(file.filename)
                destination = os.path.join(current_app.config['UPLOAD_FOLDER'],
                                           filename)
                file.save(destination)
                output = esp_get_info(destination)

    return render_template('index.html', form=form, output=output)
