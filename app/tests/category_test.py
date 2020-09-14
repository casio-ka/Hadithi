import unittest
from app.models import category

Category = category.Category

class CategoryTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Category class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_category = Category("Linda Givetash", " The U.S. ambassador to China, Terry Branstad, will be resigning ahead of November's election, Secretary of State Mike Pompeo announced Monday." ,"2020-09-14T14:01:00Z","https://www.nbcnews.com/news/world/trump-s-ambassador-china-unexpectedly-retiring-election-amid-high-tensions-n1239999.html","https://media1.s-nbcnews.com/j/newscms/2020_38/3411855/200914-terry_branstad-mc-9062_6136406ec47f10ccd22b40c8f97db88a.nbcnews-fp-1200-630.jpg","Trump's ambassador to China unexpectedly retiring before election amid high tensions - NBC News")

    def test_instance(self):
        '''
        Test to check creation of new Category instance,(is True)
        '''
        self.assertTrue(isinstance(self.new_category,Category))