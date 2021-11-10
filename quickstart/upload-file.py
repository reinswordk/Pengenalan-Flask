from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app =Flask(__name__)

@app.route('/upload')
def show_upload_form() :
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET','POST'])
def upload_file() :
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filenmae))
        return 'file uploaded successfully'
