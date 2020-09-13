from flask import Flask, render_template
from app import app
from .request import get_source

@app.route('/')
def index():

    #Getting sources
    source = get_source()
    title = 'Hadithi Hadithi'
    return render_template('index.html', title = title, sources = source)

