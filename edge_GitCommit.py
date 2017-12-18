import random
import time
from selenium import webdriver

driver = webdriver.Edge('C:\Program Files\Python\MicrosoftWebDriver.exe')
driver.get('https://github.com/santarini/seleniumPushes/blob/master/pushlog.md');
time.sleep(3)
page_body = driver.find_element_by_tag_name('body')
page_body.send_keys('e')
time.sleep(3)
js_text_box = driver.find_element_by_class_name('commit-create')
js_text_box.click()
content = driver.find_element_by_class_name('CodeMirror-code')
content.send_keys('Testing 4 5 6 \n')
time.sleep(3)
submit = driver.find_element_by_id('submit-file')
time.sleep(3)
submit.submit()
driver.quit()
