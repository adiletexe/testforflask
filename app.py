from flask import request

from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired


from findPhotos import execute  # I was created by Amir :D


app = Flask(__name__)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

app.config['SECRET_KEY'] = os.urandom(12)
app.config['UPLOAD_FOLDER'] = 'static/files'


@app.route("/index.html")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/About_us.html')
def about():
    return render_template('About_us.html')

@app.route('/Feedback.html')
def feedback():
    return render_template('Feedback.html')

'''@app.route('/Services.html', methods=['GET', 'POST'])
def services():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "the file has been uploaded successfully"
    return render_template('Services.html', form=form, x=execute())'''

@app.route('/Services.html', methods=['GET', 'POST'])
def services():
    form = UploadFileForm()
    x=[]
    if request.method == "POST":
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        x = execute()
    return render_template('Services.html', form=form, x=x)
# https://www.google.kz/search?q=2DnHWraKtR4v5vUzBbSy0FHEN23_5KfXy9zkA83dL9UpPgzFA&ie=UTF-8&oe=UTF-8&hl=en-kz&client=safari

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)