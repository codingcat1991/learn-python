# 2.	Code exercise – Calculate PnL
"""
price data: lastPrice(最新价)

timestamp,lastPrice
2020-04-10 09:31:00.000000000,5270.8
2020-04-10 09:32:00.000000000,5269.0
2020-04-10 09:33:00.000000000,5265.2
2020-04-10 09:34:00.000000000,5263.2
2020-04-10 09:35:00.000000000,5262.8
2020-04-10 09:36:00.000000000,5256.2
2020-04-10 09:37:00.000000000,5258.4

trade data: side(B means buy and S means sell), volume(手数)，price(成交价格)

tradeTime,side,volume,price
2020-04-10 13:15:14.347056383,S,1,5202.6
2020-04-10 13:20:40.948211520,B,1,5197.8
2020-04-10 13:30:28.989047356,S,1,5190.6
2020-04-10 13:30:59.830372653,B,1,5189.8
2020-04-10 13:31:45.895659721,S,1,5185.6
2020-04-10 13:34:01.851220077,B,1,5179.2
2020-04-10 13:34:29.848118690,S,1,5179.8

according to trade data, calculate the trade pnl(profit and loss) snapshot
every timestamp in price data, and draw the pnl curve picture saved in ouput

"""


def calc_pnl_and_draw_picture(price_file, trade_file, output):
    """
    :param price_file: csv file contain price data
    :param trade_file: csv file contain trade data
    :param output: output picture file
    :return: None
    """
    pass


if __name__ == "__main__":
    calc_pnl_and_draw_picture("./data/price.csv", "./data/trade.csv", "./data/pnl.png")
