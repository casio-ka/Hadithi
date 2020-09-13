from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/home')
def index():

    title = 'Hadithi Hadithi'
    return render_template('index.html', title = title)

