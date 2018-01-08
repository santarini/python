import time
import datetime
import random
from selenium import webdriver
import decimal

driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
driver.get('https://cryptowat.ch/gemini/btcusd');
time.sleep(1)
gemini_outter = driver.find_element_by_id('price-ticker')
gemini_inner = gemini_outter.get_attribute('innerHTML')
btcusdgemini = gemini_inner[len("<weak></weak><span>"):-len(" USD</span>")]
a = float(btcusdgemini)
print("Gemini BTC/USD: ", a, "USD")
time.sleep(1)
driver.get('https://cryptowat.ch/bithumb/btckrw');
bithumb_outter = driver.find_element_by_id('price-ticker')
bithumb_inner = bithumb_outter.get_attribute('innerHTML')
btckrwbithumb = bithumb_inner[len("<weak></weak><span>"):-len(" JPY</span>")]
b = float(btckrwbithumb)
print("Bithumb BTC/KRW: ", b, "KRW")
driver.get('https://www.barchart.com/forex/quotes/%5EUSDKRW');
time.sleep(1)
krwusd_out = driver.find_element_by_class_name('last-change')
krwusd_inner = krwusd_out.get_attribute('innerHTML')
c = float(krwusd_inner.replace(',',''))
print("The market USD/KRW: ", c)
d = (b/c)
print(c, " KRW is approximately ", d, " USD")
e = (d/a)
f = (((d/a)-1)* 100)
g = (300000000/c)
h = (g/4)
i = (h/e)
print("The current Arb opportunity is %.2f" % f,"%")
print("Bithumb maximum monthly withdrawal is 300,000,000 KRW or %.2f " % g," USD")
print("Ideal weekly withdrawal is %.2f " % h)
print("Given the current arb the optimal weekly deposit is %.2f " % i)
driver.quit()
