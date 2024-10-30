import yfinance as yf


class DataLoader:
    def __init__(self, ticker):
        self.ticker = ticker

    def set_ticker(self, new_ticker):
        self.ticker = new_ticker

    def get_ticker(self):
        return self.ticker

    def grab(self, start: str = "2020-01-01", end: str = "2024-01-01", interval: str = "1d", data_type=None):
        data = yf.download(self.ticker, start=start, end=end, interval=interval)
        return data[[data_type]] if data_type else data
