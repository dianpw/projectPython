import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'


# Pastikan path folder upload benar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Ambil path file ini
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'files')  # Pastikan hanya 1 level
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    
class UploadFileForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Upload File')

@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        print("Form validated!")
        file = form.file.data
        if file:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            return 'File uploaded successfully'
    else:
        print("Form errors:", form.errors)
    return render_template('upload.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)