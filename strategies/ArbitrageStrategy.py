class ArbitrageStrategy:
    def __init__(self, exchange1, exchange2):
        self.exchange1 = exchange1
        self.exchange2 = exchange2

    def find_arbitrage_opportunity(self, symbol):
        # Fetch market data from both exchanges for the given symbol
        data_exchange1 = self.exchange1.get_market_info(symbol)
        data_exchange2 = self.exchange2.get_market_info(symbol)

        # Extract relevant information such as prices, order book depth, etc.
        price_exchange1 = data_exchange1['price']
        price_exchange2 = data_exchange2['price']

        # Check for price differentials and calculate potential profit
        if price_exchange1 > price_exchange2:
            potential_profit = price_exchange1 - price_exchange2
            return {
                'exchange1': self.exchange1,
                'exchange2': self.exchange2,
                'symbol': symbol,
                'potential_profit': potential_profit
            }
        elif price_exchange2 > price_exchange1:
            potential_profit = price_exchange2 - price_exchange1
            return {
                'exchange1': self.exchange2,
                'exchange2': self.exchange1,
                'symbol': symbol,
                'potential_profit': potential_profit
            }
        else:
            return None
