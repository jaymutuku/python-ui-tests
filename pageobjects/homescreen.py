"""
__author_ = "Josphat Mutuku"
__date__ ="2019-07-03"
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import strings

class HomeScreen:
  
  def __init__(self,driver):
    self.driver = driver
    # self.driver = driver.implicitly_wait(5)
    
    self.contactField = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
By.ID, "et_pb_contact_name_0")))  
    self.contactField.send_keys("Josphat")
    
    self.messageField = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
By.ID, "et_pb_contact_message_0")))  
    self.messageField.send_keys("Please show the sitemap for ultimateqa")
    
    self.submitButton = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
By.CLASS_NAME, "et_contact_bottom_container")))  
    self.submitButton.click()
    
    self.displayedMessage = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
By.CLASS_NAME, "et-pb-contact-message")))  
      
    
  def validate_message_displayed(self):
     assert self.displayedMessage.is_displayed() 

      
    
    
