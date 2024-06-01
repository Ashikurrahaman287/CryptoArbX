from telegram import TelegramBot
from exchanges.gate import GateAPI
from exchanges.lbank import LBankAPI
from exchanges.bybit import BybitAPI
from strategies import ArbitrageStrategy
from utils import DataProcessor
from config import (GATE_API_KEY, GATE_API_SECRET,
                    LBANK_API_KEY, LBANK_API_SECRET,
                    BYBIT_API_KEY, BYBIT_API_SECRET,
                    TELEGRAM_BOT_TOKEN)


gate_api = GateAPI(GATE_API_KEY, GATE_API_SECRET)
lbank_api = LBankAPI(LBANK_API_KEY, LBANK_API_SECRET)
bybit_api = BybitAPI(BYBIT_API_KEY, BYBIT_API_SECRET)

# Initialize Telegram bot
telegram_bot = TelegramBot(TELEGRAM_BOT_TOKEN)

def main():

    gate_data = gate_api.get_market_info('BTC_USDT')
    lbank_data = lbank_api.get_market_info('btc_usdt')
    bybit_data = bybit_api.get_market_info('BTCUSD')


    gate_df = DataProcessor.preprocess_market_data(gate_data)
    lbank_df = DataProcessor.preprocess_market_data(lbank_data)
    bybit_df = DataProcessor.preprocess_market_data(bybit_data)

    # Example usage: Implement trading strategy (arbitrage)
    arbitrage_strategy = ArbitrageStrategy(gate_api, lbank_api, bybit_api)
    opportunity = arbitrage_strategy.find_arbitrage_opportunity('BTC_USDT')


    if opportunity:
        message = f'Arbitrage opportunity detected!\nExchange 1: {opportunity["exchange1"].__class__.__name__}\nExchange 2: {opportunity["exchange2"].__class__.__name__}\nPotential Profit: {opportunity["potential_profit"]} {opportunity["symbol"]}'
        telegram_bot.send_message(chat_id='your_chat_id', text=message)
    else:
        telegram_bot.send_message(chat_id='your_chat_id', text='No arbitrage opportunity found.')

if __name__ == "__main__":
    main()
