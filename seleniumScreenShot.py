from selenium import webdriver

#surfacebook and work computer webdriver path
driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe')
driver.get('https://dawson8a.onelogin.com/login')

driver.save_screenshot("testShot.png")
