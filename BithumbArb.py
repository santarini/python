import time
import datetime
import random
from selenium import webdriver

#Internal Arb

driver = webdriver.Edge('C:\Program Files\Python\Python36\MicrosoftWebDriver.exe')
driver.get('https://www.bithumb.com/');
#btc
btc_bithumb_outterHTML = driver.find_element_by_id('assetRealBTC')
btc_bithumb_innerHTML = btc_bithumb_outterHTML.get_attribute('innerHTML')
print(btc_bithumb_innerHTML)
#xrp
xrp_bithumb_outterHTML = driver.find_element_by_id('assetRealXRP')
xrp_bithumb_innerHTML = xrp_bithumb_outterHTML.get_attribute('innerHTML')
print(xrp_bithumb_innerHTML)
#eth
eth_bithumb_outterHTML = driver.find_element_by_id('assetRealETH')
eth_bithumb_innerHTML = eth_bithumb_outterHTML.get_attribute('innerHTML')
print(eth_bithumb_innerHTML)
#bch
bch_bithumb_outterHTML = driver.find_element_by_id('assetRealBCH')
bch_bithumb_innerHTML = bch_bithumb_outterHTML.get_attribute('innerHTML')
print(bch_bithumb_innerHTML)
#lch
ltc_bithumb_outterHTML = driver.find_element_by_id('assetRealLTC')
ltc_bithumb_innerHTML = ltc_bithumb_outterHTML.get_attribute('innerHTML')
print(ltc_bithumb_innerHTML)
#dash
dash_bithumb_outterHTML = driver.find_element_by_id('assetRealDASH')
dash_bithumb_innerHTML = dash_bithumb_outterHTML.get_attribute('innerHTML')
print(dash_bithumb_innerHTML)
#xmr
xmr_bithumb_outterHTML = driver.find_element_by_id('assetRealXMR')
xmr_bithumb_innerHTML = xmr_bithumb_outterHTML.get_attribute('innerHTML')
print(xmr_bithumb_innerHTML)
#eos
eos_bithumb_outterHTML = driver.find_element_by_id('assetRealEOS')
eos_bithumb_innerHTML = eos_bithumb_outterHTML.get_attribute('innerHTML')
print(eos_bithumb_innerHTML)
#qtum
qtum_bithumb_outterHTML = driver.find_element_by_id('assetRealQTUM')
qtum_bithumb_innerHTML = qtum_bithumb_outterHTML.get_attribute('innerHTML')
print(qtum_bithumb_innerHTML)
#btg
btg_bithumb_outterHTML = driver.find_element_by_id('assetRealBTG')
btg_bithumb_innerHTML = btg_bithumb_outterHTML.get_attribute('innerHTML')
print(btg_bithumb_innerHTML)
#etc
etc_bithumb_outterHTML = driver.find_element_by_id('assetRealETC')
etc_bithumb_innerHTML = etc_bithumb_outterHTML.get_attribute('innerHTML')
print(etc_bithumb_innerHTML)
#zec
zec_bithumb_outterHTML = driver.find_element_by_id('assetRealZEC')
zec_bithumb_innerHTML = zec_bithumb_outterHTML.get_attribute('innerHTML')
print(zec_bithumb_innerHTML)
driver.quit()
