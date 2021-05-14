# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from typing import Dict, List
from functools import reduce
from pandas import DataFrame
from technical.util import resample_to_interval
# --------------------------------

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib

"""
How to use?

source ./.env/bin/activate

freqtrade download-data -t 5m --timerange=20180131-20181201

freqtrade backtesting --strategy StrategySell --timeframe 5m --timerange=20180131-20181201
"""


class StrategySell(IStrategy):
    """
    Strategy 002
    How to use it?
    > python3 ./freqtrade/main.py -s Strategy001
    """

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi"
    minimal_roi = {
        "60": -1 # sell the coin 60 minutes after buy
    }

    # Optimal stoploss designed for the strategy
    # This attribute will be overridden if the config file contains "stoploss"
    stoploss = -100

    # Optimal timeframe for the strategy
    timeframe = '5m'

    # trailing stoploss
    trailing_stop = False
    trailing_stop_positive = 0.01
    trailing_stop_positive_offset = 0.02

    # run "populate_indicators" only for new candle
    process_only_new_candles = False

    # Experimental settings (configuration will overide these if set)
    use_sell_signal = True
    sell_profit_only = True
    ignore_roi_if_buy_signal = False

    # Number of candles the strategy requires before producing valid signals
    startup_candle_count: int = 5

    # Optional order type mapping
    order_types = {
        'buy': 'limit',
        'sell': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }

    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        These pair/interval combinations are non-tradeable, unless they are part
        of the whitelist as well.
        For more information, please consult the documentation
        :return: List of tuples in the format (pair, interval)
            Sample: return [("ETH/USDT", "5m"),
                            ("BTC/USDT", "15m"),
                            ]
        """
        return []


    def get_ticker_indicator(self):
        return int(self.timeframe[:-1])


    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Adds several different TA indicators to the given DataFrame
        Performance Note: For the best performance be frugal on the number of indicators
        you are using. Let uncomment only the indicator you are using in your strategies
        or your hyperopt configuration, otherwise you will waste your memory and CPU usage.
        """

        dataframe_long = resample_to_interval(dataframe, self.get_ticker_indicator() * 48)

        dataframe['ema7'] = ta.EMA(dataframe, timeperiod=7)
        dataframe['ema13'] = ta.EMA(dataframe, timeperiod=13)
        dataframe['ema21'] = ta.EMA(dataframe, timeperiod=21)
        dataframe['ema50'] = ta.EMA(dataframe, timeperiod=50)
        dataframe['ema100'] = ta.EMA(dataframe, timeperiod=100)

        heikinashi_long = qtpylib.heikinashi(dataframe_long)
        dataframe['ha_open_long'] = heikinashi_long['open']
        dataframe['ha_close_long'] = heikinashi_long['close']

        heikinashi = qtpylib.heikinashi(dataframe)
        dataframe['ha_low'] = heikinashi['low']
        dataframe['ha_high'] = heikinashi['high']

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (
                (dataframe['ha_close_long'] >= (1.7 * dataframe['ha_open_long'].shift(1))) &
                ((dataframe['ha_high'] - dataframe['ha_low']) >= (0.1 * abs(dataframe['ha_close_long'] - dataframe['ha_open_long'])))
            ),
            'buy'] = 1

        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # it's not useful

        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (
                # (dataframe['ha_close'] < dataframe['ema13']) &  # Guard: ema13 greater than open price
                # ((dataframe['ha_high'] - dataframe['ha_low']) >= (0.1 * (dataframe['ema13'])))  # Guard: ema13 smaller than close price
            ),
            'sell'] = 0
        return dataframe