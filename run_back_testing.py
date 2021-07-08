import os
import json


time_frame = "3d"
strategy1 = "Strategy005"
date_times = ["20190116-20190501"]


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def download_run_strategy():
    # date_times = ["20190116-20190501", "20190501-20191001", "20191001-20191229", "20200101-20200430", "20200101-20200130",
                  # "20200201-20200229", "20200301-20200330", "20200401-20200430", "20200501-20200830", "20200501-20200530",
                  # "20200601-20200630", "20200901-20201230", "20210101-20210515", "20210201-20210330", "20210301-20210430",
                  # "20180116-20180501", "20180501-20181001", "20181001-20181229", "20210101-",
                  # "20210201-", "20190301-20190330", "20190401-20190430", "20191201-20200830"
                  # ]
    for i in range(0, len(date_times)):
        os.system("freqtrade download-data -t " + time_frame + " --timerange=" + date_times[i])

        os.system(
            "freqtrade backtesting --strategy " + strategy1 + " --timeframe " + time_frame + " --timerange=" + date_times[i]
            + " --export trade --export-filename=user_data/backtest_results/" + strategy1 + "_" + date_times[i] + ".json")


def analyze_json():
    files = os.listdir("/Users/amir/PycharmProjects/freqtrade_amir/user_data/backtest_results/")
    files.remove(".gitkeep")
    files.remove(".last_result.json")
    # files.remove("Strategy003_20190116-20190501-2021-05-25_14-47-41.json")
    # files.remove("Strategy003_20190501-20191001-2021-05-25_14-48-58.json")

    files = sorted(files)
    for i in range(0, len(files)):
        tmp = files[i].split("_")
        if tmp[0] != strategy1:
            continue
        with open('/Users/amir/PycharmProjects/freqtrade_amir/user_data/backtest_results/' + files[i]) as f:
            data = json.load(f)

        data_dict = data
        file_detail = files[i].split("_")
        data_detail = file_detail[1].split("-")
        print("Strategy: ", file_detail[0], "from: ", data_detail[0], "to: ", data_detail[1])
        profit = data_dict['strategy_comparison'][0]["profit_total"]
        print("market_change", data_dict['strategy']['Strategy005']['market_change'])
        output = f"{profit:.9f}"
        print("profit: ", output)
        print("_________________________________")


def analyze_json_diff_days():
    files = os.listdir("/Users/amir/PycharmProjects/freqtrade_amir/user_data/backtest_results/")
    files.remove(".gitkeep")
    files.remove(".last_result.json")
    files.remove("backtest-result-2021-06-05_19-40-30.json")
    files.remove("backtest-result-2021-06-05_19-41-53.json")
    s3 = []
    s6 = []
    s9 = []
    s12 = []
    s15 = []
    s18 = []
    s21 = []
    s24 = []
    s27 = []
    s30 = []
    for i in range(0, len(files)):
        tmp = files[i].split("_")
        if tmp[0] != "Strategy003":
            continue
        if not hasNumbers(tmp[2][0:2]):
            continue
        tmp22 = tmp[2].split("-")
        if tmp22[4] != "07":
            continue
        if tmp[1] == "3":
            s3.append(files[i])
        if tmp[1] == "6":
            s6.append(files[i])
        if tmp[1] == "9":
            s9.append(files[i])
        if tmp[1] == "12":
            s12.append(files[i])
        if tmp[1] == "15":
            s15.append(files[i])
        if tmp[1] == "18":
            s18.append(files[i])
        if tmp[1] == "21":
            s21.append(files[i])
        if tmp[1] == "24":
            s24.append(files[i])
        if tmp[1] == "27":
            s27.append(files[i])
        if tmp[1] == "30":
            s30.append(files[i])

    all = []
    all.append(s3)
    all.append(s6)
    all.append(s9)
    all.append(s12)
    all.append(s15)
    all.append(s18)
    all.append(s21)
    all.append(s24)
    all.append(s27)
    all.append(s30)

    for i in range(len(all)):
        print(len(all[i]))

    res_file = []
    res = []
    res_market_change = []
    for i in range(len(all)):
        all[i] = sorted(all[i])
        for j in range(len(all[i])):

            with open('/Users/amir/PycharmProjects/freqtrade_amir/user_data/backtest_results/' + all[i][j]) as f:
                data = json.load(f)

            data_dict = data
            profit = data_dict['strategy_comparison'][0]["profit_total"]
            output = f"{profit:.9f}"
            market_change = data_dict['strategy']['Strategy003']['market_change']
            if i == 0:
                tmp = []
                tmp.append(all[i][j])
                res_file.append(tmp)
                tmp2 = []
                tmp2.append(profit*100)
                res.append(tmp2)
                res_market_change.append(market_change)
            else:
                res_file[j].append(all[i][j])
                res[j].append(profit*100)

    # for i in range(len(res_market_change)):
    #     print(res_market_change[i]*100)

    # print(res_file)

    # print days and other information
    # for i in range(len(res[0])):
    #     tmp = []
    #     tmp2 = []
    #     for j in range(len(res)):
    #         tmp.append(res[j][i])
    #         str_tmp = res_file[j][i].split("_")
    #         str_tmp2 = str_tmp[2].split("-")
    #         tmp2.append(str_tmp2[0] + "-" + str_tmp2[1])
    #     print(sum(tmp))
    #     for j in range(len(tmp2)):
    #         # print(tmp2[j])

    from pandas import DataFrame
    res_pd = DataFrame(res)
    # print(res_pd)
    res_pd.to_csv("back.csv")


if __name__ == '__main__':
    print("type strategy name: (Ex: Strategy005)")
    strategy1 = input()
    print("type time_frame: (Ex: 3d)")
    time_frame = input()
    print("type date-time: (ex: 20190116-20190501)")
    date_times = []
    date_times.append(input())

    download_run_strategy()
    analyze_json()
    # analyze_json_diff_days()