#!/usr/bin/env python

from flask import Flask, request, redirect, flash, render_template
from fastai.vision import load_learner, open_image
from secrets import token_urlsafe

app = Flask(__name__)
app.secret_key = token_urlsafe(16)
learn = load_learner('./')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            image = open_image(file)
            prediction = str(learn.predict(image)[0])
            if prediction == 'villager':
                flash('It\'s a villager!')
            else:
                flash('It\'s not a villager!')
    return render_template('upload_image.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
