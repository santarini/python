import time
import datetime
import random
from selenium import webdriver

driver = webdriver.Edge('C:\Program Files\Python\MicrosoftWebDriver.exe')
driver.get('https://github.com/santarini/seleniumPushes/blob/master/pythonlog.md');
time.sleep(3)
page_body = driver.find_element_by_tag_name('body')
page_body.send_keys('e')
time.sleep(3)
js_text_box = driver.find_element_by_class_name('commit-create')
js_text_box.click()
content = driver.find_element_by_class_name('CodeMirror-code')
timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content.send_keys('* <b>' + timenow + '</b> >> Testing 1 2 3; \n')
time.sleep(3)
submit = driver.find_element_by_id('submit-file')
time.sleep(3)
submit.submit()
driver.quit()
