import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#creates a browser
driver = webdriver.Edge('C:\Program Files\Python\Python36\\MicrosoftWebDriver.exe')  # Optional argument, if not specified will search path.
#navigates to a gmail
driver.get('https://mail.google.com/mail/u/0/#inbox');
time.sleep(5) # Let the user actually see something!
#defines the body element of the page
page_body = driver.find_element_by_tag_name('body')
#creates new message
page_body.send_keys('c')
#define the "recipient" field
recipient = driver.find_element_by_name('to')
recipient.send_keys(#reciving email)
#define the "subject line" field
subject = driver.find_element_by_name('subjectbox')
timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subject.send_keys("Application completed" + Keys.TAB)
#define the "body" field
emailBody = driver.find_element_by_id(":90")
emailBody.send_keys(timenow)
#define the send button and click it
sendButton = driver.find_element_by_id(":7n")
sendButton.click()
#close the program
driver.quit()
