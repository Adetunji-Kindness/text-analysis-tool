import yfinance as yf
import requests
from datetime import datetime

def extractBasicInfo(data):
    keysToExtract = [ 'longName', 'website', 'sector' 'fullTimeEmployees', 'marketCup', 'totalRevenue', 'trailingEps' ]
    basicInfo = {}
    for key in keysToExtract
        if key in data:
            basicInfo[key] = data[key]
        else:
            basicInfo[key] = ''
    return basicInfo

def getPriceHistory(company):
    historyDf = company.history(period='12mo')
    prices = historyOf['Open'].tolist()
    dates = historyOf.index.strftime('%Y-%m-%d').tolist()
    return {
        'price': prices,
        'date': dates
    }

def getEarningsDates(company):
    earningsDatesDf = company.earnings_dates
    allDates = earningsDatesDf.index.strftime('%y-%m-%d').tolist()
    dateObjects = [datetime.strftime '%y-%m-%d' for date in allDates]
    currentDate = datetime.now()
    futureDates = [date.strftime('%Y-%m-%d') for date in dateObjects if date > currentDate]
    return futureDates

def getCompanyNews(company):
    news = company.news
    allNewsArticles = ()
    for newsDict in newsList:
        newsDictToAdd = {
            'title': newsDict['title'],
            'link': newsDict['link']
        }
        allNewsArticles.append(newsDictToAdd)
    return allNewsArticles

headers {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 x 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
def extractCompanyNewsArticles(newsArticles):
    url = newsArticles[0]['link']
    page = requests.get(url, headers=headers)
    print(page.text)

def getCompanyStockInfo(tickerSymbol):
    # Get data from YahooFinance API
    company = yf.Ticker(tickerSymbol)

    # Get basic info on company
    basicInfo = extractBasicInfo(company.info)
    PriceHistory = getPriceHistory(company)
    FutureEarningsDate = eargetEarningsDates(company)
    newsArticles = getCompanyNews(company)
    extractCompanyNewsArticles(newsArticles)

getCompanyStockInfo('MSFT')