# Built-in libraries.
import time

# Third-party libraries.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class TestEdgeSearch:
    '''
    Test cases for searching a webpage in Microsoft Edge.
    '''

    def setup_method(self):
        '''
        Executed before each method.
        '''

        # Start an Edge session.
        self.driver = webdriver.Edge()

        def teardown_method(self):
            '''
            Executed after each method.
            '''

            # End the Edge session
            self.driver.quit()


        def test_search(self):
            self.driver.get('https://www.google.com/')
            element_search = self.driver.find_element(By.NAME, 'q')
            element_search.send_keys('pytest')
            element_search.send_keys(Keys.ENTER)
            hyperlink = self.driver.find_element(
                By.XPATH,
                "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3"
            )
            hyperlink.click()
            assert 'pytest' in self.driver.title


#TODO: explore waiting strategies (implicit, explicit)