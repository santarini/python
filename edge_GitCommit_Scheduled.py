import schedule
import time
import datetime
import random
from selenium import webdriver

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]

def job():
    rand1 = random.randint(0, 20)
    i = 1
    dayofWeek = datetime.datetime.today().weekday()
    fullDate = datetime.datetime.now().strftime("%Y-%m-%d")
    print(weekdays[dayofWeek] + " " + fullDate + ": " +str(rand1) + " Pushes Scheduled")
    f = open("GitLog.txt","a")
    f.write(weekdays[dayofWeek] + " " + fullDate + ": " +str(rand1) + " Pushes Scheduled \n")
    f.close()
    driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
    while i <= rand1:
        rand2 = random.randint(0, 20)
        time.sleep(rand2)
        driver.get('https://github.com/santarini/seleniumPushes/blob/master/AutomatedPythongLog.md')
        page_body = driver.find_element_by_tag_name('body')
        page_body.send_keys('e')
        time.sleep(10)#necessary sleep time for page to load
        js_text_box = driver.find_element_by_class_name('commit-create')
        js_text_box.click()
        content = driver.find_element_by_class_name('CodeMirror-code')
        timeNow = datetime.datetime.now().strftime("%H:%M:%S")
        content.send_keys('* <b>' + fullDate + " " + timeNow + '</b> >> Office Computer; \n')
        time.sleep(3) #necessary sleep time for send_keys to fully run
        submit = driver.find_element_by_id('submit-file')
        submit.submit()
        print(str(i) + ") Completed: " + timeNow)
        f = open("GitLog.txt","a")
        f.write(str(i) + ") Completed: " + timeNow + "\n")
        f.close()
        i+=1
    driver.quit()
    print("Program Succesfully Executed: " + weekdays[dayofWeek] + " " + fullDate + " " + str(i-1) + " Pushes \n")


    
schedule.every().day.at("15:48").do(job)

while True:
    schedule.run_pending()
    #time.sleep(60) # wait one minute
