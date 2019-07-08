"""
__author_ = "Josphat Mutuku"
__date__ ="2019-07-03"
"""
import unittest

from webdriver import Driver
from values import strings
from pageobjects.homescreen import HomeScreen

class verifyMessageTest(unittest.TestCase):
  
  def setUp(self):
    self.driver = Driver()
    self.driver.navigate(strings.base_url)
    
  def test_displayedMessage(self):
    home_screen = HomeScreen(self.driver)    
    home_screen.validate_message_displayed()
        
  def tearDown(self):
    self.driver.instance.quit()     
   

if __name__ == '__main__':
  unittest.main()    