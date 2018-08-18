import time
import datetime
import clipboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


#creates a browsers
driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe')
#driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
#navigates to a gmail
driver.get('https://mail.google.com/mail/u/0/#inbox')

time.sleep(5)
page_body = driver.find_element_by_tag_name('body')

loginField = driver.find_element_by_id('identifierId')
nextButton = driver.find_element_by_id('identifierNext')
loginField.send_keys('user login')
nextButton.click()
time.sleep(3)

passwordField = driver.find_element_by_name('password')
passwordField.send_keys('user pass')
nextButton = driver.find_element_by_id('passwordNext')
nextButton.click()

time.sleep(5)
page_body = driver.find_element_by_tag_name('body')

#create new message
page_body.send_keys('c')

#define the "recipient" field
time.sleep(3)
recipient = driver.find_element_by_name('to')
recipient.send_keys('receving addrs')

#define the "subject line" field
subject = driver.find_element_by_name('subjectbox')
timenow = datetime.datetime.now().strftime("%I:%M:%S %p")
datenow = datetime.datetime.now().strftime("%Y-%m-%d")
subject.send_keys("Timecard Submitted" + Keys.TAB + timenow + " for week of X")

time.sleep(2)

attachButton = driver.find_element_by_xpath('//*[@data-tooltip = "Attach files"]')
attachButton.click()

time.sleep(3)



##clipboard.copy("C:\\Users\\m4k04\\Desktop\\TimeCardConfirmation.png")
##time.sleep(3)
##clipboard.paste()

pyautogui.typewrite(r"C:\Users\m4k04\Desktop\TimeCardConfirmation.png")
pyautogui.typewrite(['enter'])

time.sleep(3)

sendButton = driver.find_element_by_xpath('//*[@data-tooltip="Send ‪(Ctrl-Enter)‬"]')
sendButton.click()

driver.quit()

print("Done.")
