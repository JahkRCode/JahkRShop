

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains ## MAYBE
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randint, randrange
import time 
import random
from myInfo import myInfo

AMAZON_URL = 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_1?dchild=1&keywords=playstation+5&qid=1605750925&rnid=2941120011&s=videogames&sr=1-1'
AMAZON_TEST_URL = 'https://www.amazon.com/PlayStation-Console-Remastered-Bundle-Renewed-4/dp/B08DP5P4SY/ref=sr_1_1?dchild=1&keywords=playstation+4&qid=1605758562&s=videogames&sr=1-1'
WAIT_TIME = 5
PRICE_LIMIT = 700.00

class JahkRShop:
    def __init__(self, username, password):
        """ Initializes Bot with class-wide variables. """
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
    
    ## Sign into site with the product
    def signIn(self):
        """ Sign into site with the product. """
        driver = self.driver ## Navigate to URL
        
        ## Enter Username
        username_elem = driver.find_element_by_xpath("//input[@name='email']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        username_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
        ## Enter Password
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        password_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
    ## Find product under X amount
    def findProduct(self):
        """ Finds the product with global link. """
        driver = self.driver
        driver.get(AMAZON_TEST_URL)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
        ## If the product is not available, wait until it is available
        isAvailable = self.isProductAvailable()
        
        if isAvailable == 'Currently unavailable.':
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
        elif isAvailable <= PRICE_LIMIT:
            ## Buy Now
            buy_now = driver.find_element_by_name('submit.buy-now')
            buy_now.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.signIn()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            
            ## Place Order
            place_order = driver.find_element_by_name('placeYourOrder1').text
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            print(f'***** PLACE ORDER: {place_order}')
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            ## place_order.click()
            ## time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            
        else:
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
            
    def isProductAvailable(self):
        """ Checks if product is available. """
        driver = self.driver
        available = driver.find_element_by_class_name('a-color-price').text
        if available == 'Currently unavailable.':
            print(f'***** AVAILABLE: {available}')
            return available
        else:
            print(f'***** PRICE: {available}')
            return float(available[1:]) ## $123.22 -> 123.22
    
    def closeBrowser(self):
        """ Closes browser """
        self.driver.close()
        

if __name__ == '__main__':
    shopBot = JahkRShop(username=myInfo.username(), password=myInfo.password())
    shopBot.findProduct()
    shopBot.closeBrowser()
            