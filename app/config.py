class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCES_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True