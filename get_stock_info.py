import yfinance as yf


def get_stock_info(stock_ticker):
    ticker = yf.Ticker(stock_ticker)

    return {
        'ask': ticker.info['ask'],
        'bid': ticker.info['bid']
    }