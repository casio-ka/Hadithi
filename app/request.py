from app import app

#Getting api key
api_key = app.config['NEWS_API_KEY']
#Getting Sources url
source_url = app.config ['NEWS_API_SOURCE_URL']
#Getting Top Headlines
category_url = app.config ['NEWS_API_TOP_HEADLINES_URL']
