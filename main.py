# Built-in libraries.
import time

# Third-party libraries.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def automate():
    '''
    This function shows an example of web automation using Selenium. 

    To make assertions, use pytest. 
    '''
    
    # Start a Microsoft Edge session.
    driver = webdriver.Edge()

    # Navigate to a URL. 
    driver.get('https://www.google.com/')

    # Identify HTML element using the By class.
    element_search = driver.find_element(By.NAME, 'q')

    # Interact with HTML element. Access keys with the Keys class.
    element_search.send_keys('search')
    element_search.send_keys(Keys.ENTER)

    # Pause ten seconds before closing session.
    time.sleep(10)

    # End Microsoft Edge session.
    driver.quit()


if __name__ == '__main__':
    automate()