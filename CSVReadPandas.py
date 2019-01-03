import pandas

#read the csv file
ticker_df = pandas.read_csv('nasdaqList.csv')
#get all of the tickers and put them in a list
allTickers = list(ticker_df['Symbol'].values
#get the lenght of the list
tickerCount = len(ticker_df['Symbol'].values)

                  
print(ticker_df['Symbol'].values)
print(len(ticker_df['Symbol'].values))
print(type(list(ticker_df['Symbol'].values)))
