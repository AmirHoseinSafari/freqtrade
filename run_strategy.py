from pathlib import Path
from freqtrade.configuration import Configuration
import os


pairs_all = ["1INCH/BTC", "AVA/BTC", "CELR/BTC", "DOCK/BTC", "FUN/BTC", "KAVA/BTC", "NAS/BTC", "PHB/BTC", "RVN/BTC", "TCT/BTC", "WAVES/BTC", "AAVE/BTC", "AXS/BTC", "CFX/BTC", "DODO/BTC", "FXS/BTC", "NAV/BTC", "SALT/BTC", "TFUEL/BTC", "WBTC/BTC", "ACM/BTC", "BADGER/BTC", "CHAT/BTC", "DOGE/BTC", "GAS/BTC", "KMD/BTC", "NBS/BTC", "PIVX/BTC", "SAND/BTC", "THETA/BTC", "WINGS/BTC", "ADA/BTC", "BAL/BTC", "CHR/BTC", "DOT/BTC", "GLM/BTC", "KNC/BTC", "NCASH/BTC", "PNT/BTC", "SCRT/BTC", "TKO/BTC", "WING/BTC", "ADX/BTC", "BAND/BTC", "CHZ/BTC", "DREP/BTC", "GNT/BTC", "KSM/BTC", "NEAR/BTC", "POA/BTC", "SC/BTC", "TLM/BTC", "WIN/BTC", "AERGO/BTC", "BAT/BTC", "CKB/BTC", "DUSK/BTC", "GO/BTC", "LEND/BTC", "NEBL/BTC", "POE/BTC", "SFP/BTC", "TNB/BTC", "WNXM/BTC", "AE/BTC", "BCC/BTC", "CLOAK/BTC", "EASY/BTC", "GRS/BTC", "LINA/BTC", "NEO/BTC", "POLY/BTC", "SKL/BTC", "TNT/BTC", "WPR/BTC", "AGI/BTC", "BCD/BTC", "CMT/BTC", "EDO/BTC", "GRT/BTC", "LINK/BTC", "NKN/BTC", "POND/BTC", "SKY/BTC", "TOMO/BTC", "WRX/BTC", "AION/BTC", "BCH/BTC", "CND/BTC", "EGLD/BTC", "GTO/BTC", "LIT/BTC", "NMR/BTC", "POWR/BTC", "SNGLS/BTC", "TRB/BTC", "WTC/BTC", "AKRO/BTC", "BCN/BTC", "COCOS/BTC", "ELF/BTC", "GVT/BTC", "LOOM/BTC", "NPXS/BTC", "PPT/BTC", "SNM/BTC", "TRIG/BTC", "XEM/BTC", "ALGO/BTC", "BCPT/BTC", "COMP/BTC", "ENG/BTC", "GXS/BTC", "LRC/BTC", "NULS/BTC", "PSG/BTC", "SNT/BTC", "TROY/BTC", "XLM/BTC", "ALICE/BTC", "BEAM/BTC", "COS/BTC", "ENJ/BTC", "HARD/BTC", "LSK/BTC", "NXS/BTC", "QKC/BTC", "SNX/BTC", "TRU/BTC", "XMR/BTC", "ALPHA/BTC", "BEL/BTC", "COTI/BTC", "EOS/BTC", "HBAR/BTC", "LTC/BTC", "OAX/BTC", "QLC/BTC", "SOL/BTC", "TRX/BTC", "XRP/BTC", "AMB/BTC", "BLZ/BTC", "CRV/BTC", "EPS/BTC", "HC/BTC", "LTO/BTC", "OCEAN/BTC", "QSP/BTC", "SRM/BTC", "TUSD/BTC", "XTZ/BTC", "ANKR/BTC", "BNB/BTC", "CTK/BTC", "ERD/BTC", "HIVE/BTC", "LUNA/BTC", "OGN/BTC", "QTUM/BTC", "STEEM/BTC", "TVK/BTC", "XVG/BTC", "ANT/BTC", "BNT/BTC", "CTSI/BTC", "ETC/BTC", "HNT/BTC", "LUN/BTC", "OG/BTC", "RAMP/BTC", "STMX/BTC", "TWT/BTC", "XVS/BTC", "APPC/BTC", "BOT/BTC", "CTXC/BTC", "ETH/BTC", "HOT/BTC", "MANA/BTC", "OMG/BTC", "RCN/BTC", "STORJ/BTC", "UMA/BTC", "XZC/BTC", "ARDR/BTC", "BQX/BTC", "CVC/BTC", "EVX/BTC", "HSR/BTC", "MATIC/BTC", "OM/BTC", "RDN/BTC", "STORM/BTC", "UNFI/BTC", "YFII/BTC", "ARK/BTC", "BRD/BTC", "DAI/BTC", "FET/BTC", "ICN/BTC", "MBL/BTC", "ONE/BTC", "REEF/BTC", "STPT/BTC", "UNI/BTC", "YFI/BTC", "ARN/BTC", "BSV/BTC", "DASH/BTC", "FIL/BTC", "ICX/BTC", "MCO/BTC", "ONG/BTC", "RENBTC/BTC", "STRAT/BTC", "UTK/BTC", "YOYOW/BTC", "ARPA/BTC", "BTCB/BTC", "DATA/BTC", "FIO/BTC", "IDEX/BTC", "MDA/BTC", "ONT/BTC", "REN/BTC", "STRAX/BTC", "VEN/BTC", "ZEC/BTC", "ASR/BTC", "BTCST/BTC", "DCR/BTC", "FIRO/BTC", "INJ/BTC", "MDT/BTC", "ORN/BTC", "REP/BTC", "STX/BTC", "VET/BTC", "ZEN/BTC", "AST/BTC", "BTG/BTC", "DEGO/BTC", "FIS/BTC", "INS/BTC", "MFT/BTC", "OST/BTC", "REQ/BTC", "SUB/BTC", "VIA/BTC", "ZIL/BTC", "ATM/BTC", "BTS/BTC", "DENT/BTC", "FLM/BTC", "IOST/BTC", "MITH/BTC", "OXT/BTC", "RIF/BTC", "SUN/BTC", "VIBE/BTC", "ZRX/BTC", "ATOM/BTC", "BTT/BTC", "DGB/BTC", "FOR/BTC", "IOTA/BTC", "MKR/BTC", "PAXG/BTC", "RLC/BTC", "SUPER/BTC", "VIB/BTC", "AUCTION/BTC", "BZRX/BTC", "DGD/BTC", "FRONT/BTC", "IOTX/BTC", "MOD/BTC", "PAX/BTC", "ROSE/BTC", "SUSD/BTC", "VIDT/BTC", "AUDIO/BTC", "CAKE/BTC", "DIA/BTC", "FTM/BTC", "IRIS/BTC", "MTH/BTC", "PERL/BTC", "RPX/BTC", "SUSHI/BTC", "VITE/BTC", "AUTO/BTC", "CDT/BTC", "DLT/BTC", "FTT/BTC", "JST/BTC", "MTL/BTC", "PERP/BTC", "RSR/BTC", "SXP/BTC", "WABI/BTC", "AVAX/BTC", "CELO/BTC", "DNT/BTC", "FUEL/BTC", "JUV/BTC", "NANO/BTC", "PHA/BTC", "RUNE/BTC", "SYS/BTC", "WAN/BTC"]

# pairs_all = ["ETH/BTC"]


def download_data(timeFrame):
    # os.system('source ./.env/bin/activate \n freqtrade download-data --days 20 -t 3d')
    os.system('freqtrade download-data --days 200 --data-format-ohlcv hdf5 -t ' + timeFrame)


def run_sterategy(timeFrame, num_of_candles, strategy_num):
    buy_signals = []
    # Initialize empty configuration object

    # config = Configuration.from_files([])
    # Optionally, use existing configuration file
    config = Configuration.from_files([])

    # Define some constants
    config["timeframe"] = timeFrame
    # Name of the strategy class
    config["strategy"] = "Strategy00" + str(strategy_num)
    # Location of the data
    data_location = Path(config['user_data_dir'], 'data', 'binance')
    # Pair to analyze - Only use one pair here
    pairs = pairs_all


    # Load data using values set above
    from freqtrade.data.history import load_pair_history

    for i in range(0, len(pairs)):
        try:
            pair = pairs[i]
            print(pair)
            candles = load_pair_history(datadir=data_location,
                                        timeframe=config["timeframe"],
                                        pair=pair,
                                        data_format="hdf5",
                                        )

            # Confirm success
            print("Loaded " + str(len(candles)) + f" rows of data for {pair} from {data_location}")
            # candles.head()

            # Load strategy using values set above
            from freqtrade.resolvers import StrategyResolver

            strategy = StrategyResolver.load_strategy(config)
            strategy.timeframe = config["timeframe"]
            strategy.startup_candle_count = num_of_candles
            # Generate buy/sell signals using strategy

            df = strategy.analyze_ticker(candles, {'pair': pair})
            # print(df)
            last_row_df = df.iloc[-3:]
            # print(last_row_df)
            if last_row_df.iloc[0]['buy'] == 1 or last_row_df.iloc[0]['buy'] == 1 or last_row_df.iloc[0]['buy'] == 1:
                buy_signals.append(pair)
            # print(buy_signals)
        except:
            print("Error in finding:", pair)
    # print(buy_signals)
    return buy_signals


def main_function(timeFrame, num_of_candles, strategy_num):
    download_data(timeFrame)
    return run_sterategy(timeFrame, num_of_candles, strategy_num)


if __name__ == '__main__':
    timeFrame = '3d'
    num_of_candles = 2
    strategy_num = 2
    # download_data(timeFrame)
    print(run_sterategy(timeFrame, num_of_candles, strategy_num))
    # ['1INCH/BTC', 'DOGE/BTC', 'DOT/BTC', 'BAND/BTC', 'DREP/BTC', 'TNB/BTC', 'WNXM/BTC', 'EASY/BTC', 'NEO/BTC',
    #  'BCD/BTC', 'LINK/BTC', 'NKN/BTC', 'WRX/BTC', 'BCH/BTC', 'EGLD/BTC', 'NMR/BTC', 'COMP/BTC', 'XLM/BTC', 'XMR/BTC',
    #  'EOS/BTC', 'LTC/BTC', 'XRP/BTC', 'SRM/BTC', 'XTZ/BTC', 'ETC/BTC', 'TWT/BTC', 'ETH/BTC', 'UMA/BTC', 'YFII/BTC',
    #  'UNI/BTC', 'YFI/BTC', 'DASH/BTC', 'ZEC/BTC', 'INJ/BTC', 'ZEN/BTC', 'MITH/BTC', 'ATOM/BTC', 'MKR/BTC', 'CELO/BTC']
