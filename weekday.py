import datetime
import requests
import bs4 as bs
from datetime import datetime, timedelta

#figure out today's date and the first and last day of this week

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
today = datetime.today().weekday()
todayDate = datetime.today()
beginWeek = datetime.today() - timedelta(days=(today+1))
endWeek = beginWeek + timedelta(days=6)

#make a list for all dates in this week
datesInWeek =[]

for x in range (0, 7):
    datesInWeek.append((beginWeek + timedelta(days = x)).strftime('%Y-%m-%d'))

#perform main function for each day in week
for x in range (0, 7):
    response = requests.get('https://finance.yahoo.com/calendar/ipo?from=' + beginWeek.strftime("%Y-%m-%d") +' &to=' + endWeek.strftime("%Y-%m-%d") + '&day=' + datesInWeek[x] )
    soup = bs.BeautifulSoup(response.text, 'lxml')
    for table in soup.findAll('table'):
        for tbody in table.findAll('tbody'):
            for tr in table.findAll('tr'):
                if tr.find('th'):
                    continue
                else:
                    ticker = tr.findAll("td")[0]
                    companyName = tr.findAll("td")[1]
                    indexName = tr.findAll("td")[2]
                    ipoDate = tr.find("span")
                    price = tr.findAll("td")[3]
                    priceRange = tr.findAll("td")[4]
                    currency = tr.findAll("td")[5]
                    shares = tr.findAll("td")[6]
                    actions = tr.findAll("td")[7]
                    print(ticker.text)
                    print(companyName.text)
                    print(indexName.text)
                    print(ipoDate.text)
                    print(price.text)
                    print(priceRange.text)
                    print(currency.text)
                    print(shares.text)
                    print(actions.text)
