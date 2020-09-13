from app import app
from models import source

#Getting api key
api_key = app.config['NEWS_API_KEY']
#Getting Sources url
source_url = app.config ['NEWS_API_SOURCE_URL']
#Getting Top Headlines
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

        if get_sources_response['sources']:
            source_results_list = get_sourcs_response['sources']
            source_results = process_results(source_results_list)


    return source_results