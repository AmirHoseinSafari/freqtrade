from pathlib import Path
from freqtrade.configuration import Configuration
import os
import sys

time_frame = "5m"
strategy1 = "Strategy004"
strategy2 = "StrategySell"


date_times = ["20190116-20190501", "20190501-20191001", "20191001-20191229", "20200101-20200430", "20200101-20200130",
              "20200201-20200229", "20200301-20200330", "20200401-20200430", "20200501-20200830", "20200501-20200530",
              "20200601-20200630", "20200901-20201230", "20210101-20210515", "20210201-20210330", "20210301-20210430"]


for i in range(0, len(date_times)):
    os.system("freqtrade download-data -t " + time_frame + " --timerange=" + date_times[i])

    os.system(
        "freqtrade backtesting --strategy " + strategy1 + " --timeframe " + time_frame + " --timerange=" + date_times[i]
        + " --export trade --export-filename=user_data/backtest_results/" + strategy1 + "_" + date_times[i] + ".json")

    os.system(
        "freqtrade backtesting --strategy " + strategy2 + " --timeframe " + time_frame + " --timerange=" + date_times[i]
        + " --export trade --export-filename=user_data/backtest_results/" + strategy2 + "_" + date_times[i] + ".json")
