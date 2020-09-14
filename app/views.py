from flask import Flask, render_template
from app import app
from .request import get_source, article_source, get_headlines, get_category

@app.route('/')
def index():

    #Getting sources
    source = get_source()
    headlines = get_headlines()
    title = 'Hadithi Hadithi'
    return render_template('index.html', title = title, sources = source, headlines = headlines)

@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    source = get_source()
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id, sources = source)

@app.route('/categories/<category_name>')
def category(category_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(category_name)
    title = f'{category_name}'
    name = category_name
    source = get_source()
    return render_template('categories.html',title = title, category = category, name= category_name, sources = source)