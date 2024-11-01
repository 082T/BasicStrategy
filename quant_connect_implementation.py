from AlgorithmImports import *

SHORT_WINDOW = 7
LONG_WINDOW = 189

class SMACrossStrategy(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2010, 1, 1)
        self.set_cash(1000)
        
        self.spy = self.add_equity("SPY", Resolution.Daily).symbol

        assert SHORT_WINDOW < LONG_WINDOW

        self.short_sma = self.sma(self.spy, SHORT_WINDOW, Resolution.Daily)
        self.long_sma = self.sma(self.spy, LONG_WINDOW, Resolution.Daily)

        self.history(self.spy, LONG_WINDOW, Resolution.Daily)

    def on_data(self, data: Slice):
        if not self.short_sma.is_ready or not self.long_sma.is_ready:
            return
        short_sma_value = self.short_sma.current.value
        long_sma_value = self.long_sma.current.value
        if short_sma_value > long_sma_value:
            self.set_holdings(self.spy, 1)
        elif short_sma_value < long_sma_value:
            self.liquidate(self.spy)
