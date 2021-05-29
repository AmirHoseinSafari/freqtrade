import json
import os


files = os.listdir("/Users/amir/PycharmProjects/freqtrade_amir/user_data/backtest_results/")
files.remove(".gitkeep")
files.remove(".last_result.json")
files.remove("Strategy003_20190116-20190501-2021-05-25_14-47-41.json")
files.remove("Strategy003_20190501-20191001-2021-05-25_14-48-58.json")

files = sorted(files)
for i in range(0, len(files)):
    with open('/Users/amir/PycharmProjects/freqtrade_amir/user_data/backtest_results/' + files[i]) as f:
        data = json.load(f)

    data_dict = data
    print(files[i])
    profit = data_dict['strategy_comparison'][0]["profit_total"]
    output = f"{profit:.9f}"
    print(output)

