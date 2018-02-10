import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#creates a browsers
#driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe')
driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
#navigates to a gmail
driver.get('https://mail.google.com/mail/u/3/');
#defines the body element of the page
time.sleep(5)
page_body = driver.find_element_by_tag_name('body')
#creates new message
page_body.send_keys('c')
#define the "recipient" field
time.sleep(1)
recipient = driver.find_element_by_name('to')
recipient.send_keys('enter reciving email or phone number here')
#define the "subject line" field
subject = driver.find_element_by_name('subjectbox')
timenow = datetime.datetime.now().strftime("%I:%M:%S %p")
datenow = datetime.datetime.now().strftime("%Y-%m-%d")
subject.send_keys("Application completed" + Keys.TAB + timenow)
time.sleep(2)
#define the "body" field
#emailBody = driver.find_element_by_id(":90")
#emailBody.send_keys(timenow)
#define the send button and click it
sendButton = driver.find_element_by_id(":7n")
sendButton.click()
#close the programe
time.sleep(5)
driver.quit()
