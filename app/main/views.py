from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source, article_source, get_headlines, get_category, search_article

@main.route('/')
def index():

    #Getting sources
    source = get_source()
    headlines = get_headlines()
    title = 'Hadithi Hadithi'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
        return render_template('index.html', title = title, sources = source, headlines = headlines)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    source = get_source()
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id, sources = source)

@main.route('/categories/<category_name>')
def category(category_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(category_name)
    title = f'{category_name}'
    name = category_name
    source = get_source()
    return render_template('categories.html',title = title, category = category, name= category_name, sources = source)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',sources = searched_articles)