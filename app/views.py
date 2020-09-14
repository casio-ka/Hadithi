from flask import Flask, render_template
from app import app
from .request import get_source, article_source

@app.route('/')
def index():

    #Getting sources
    source = get_source()
    title = 'Hadithi Hadithi'
    return render_template('index.html', title = title, sources = source)

@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )