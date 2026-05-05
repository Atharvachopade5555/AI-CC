#pip install flask
#pip install cryptography

from flask import Flask, request, render_template
import cloud_controller as cc
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():

    if 'file' not in request.files:
        return "No file selected"

    file = request.files['file']

    if file.filename == '':
        return "No file selected"

    filename = file.filename

    file.save(filename)

    cc.upload(filename)

    return "File Uploaded Successfully"

@app.route('/download', methods=['POST'])
def download():

    filename = request.form['filename']

    if filename == '':
        return "Enter filename"

    cc.download(filename)

    return "File Downloaded Successfully"

app.run(host="0.0.0.0", port=5000, debug=True)