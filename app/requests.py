import urllib.request,json
from .models import Source, Article, Headlines


#Getting api key
api_key = None
#Getting Sources url
source_url = None
#Getting Top Headlines
category_url = None 

def configure_request(app):
    global api_key,source_url,category_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config ['NEWS_API_SOURCE_URL']
    category_url = app.config ['NEWS_API_TOP_HEADLINES_URL']


def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = source_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if  get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    function to process the source result and transform them to a list of objects
    Args:
        source_list:dictionary containing source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        if id:
            source_object = Source(id,name,description,url,category,language)
            source_results.append(source_object)

    return source_results

def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if  article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(article_list):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in article_list:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results

def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if  get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)

    return get_headlines_results


def process_headlines_results(headlines_list):
    '''
    function that processes the json files of headlines from the api key
    '''
    get_headlines_results = []
    for headlines in headlines_list:
        author = headlines.get('author')
        description = headlines.get('description')
        time = headlines.get('publishedAt')
        url = headlines.get('url')
        image = headlines.get('urlToImage')
        title = headlines.get ('title')

        if url:
            headline_objects = Headlines(author,description,time,url,image,title)
            get_headlines_results.append(headline_objects)

    return get_headlines_results

def get_category(category_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = category_url.format(category_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)

    return get_cartegory_results

def search_article(source_name):
    '''
    function that searches the app using the app name
    ''' 
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(source_name,api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_source_data=url.read()
        search_article_response = json.loads(search_source_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_articles_results(search_article_list)
    
    return search_article_results

