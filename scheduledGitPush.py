import schedule
import time
import datetime
import random
from selenium import webdriver

def job(t):
    driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
    driver.get('https://github.com/santarini/seleniumPushes/blob/master/AutomatedPythongLog.md');
    page_body = driver.find_element_by_tag_name('body')
    page_body.send_keys('e')
    time.sleep(10)#necessary sleep time for page to load
    js_text_box = driver.find_element_by_class_name('commit-create')
    js_text_box.click()
    content = driver.find_element_by_class_name('CodeMirror-code')
    timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.send_keys('* <b>' + timenow + '</b> >> Testing 1 2 3; \n')
    time.sleep(1) #necessary sleep time for send_keys to fully run
    submit = driver.find_element_by_id('submit-file')
    submit.submit()
    driver.quit()
    print("done")

schedule.every().day.at("09:50").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
