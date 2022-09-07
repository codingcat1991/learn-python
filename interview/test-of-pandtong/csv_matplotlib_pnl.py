import csv
import matplotlib.pyplot as plt


def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data


# def calc_pnl(prices,trades):


def calc_pnl_and_draw_picture(price_file, trade_file, output):
    """
    :param price_file: csv file contain price data
    :param trade_file: csv file contain trade data
    :param output: output picture file
    :return: None
    """
    prices = read_csv_file(price_file)
    trades = read_csv_file(trade_file)
    prices_trades = []
    for item in zip(prices, trades):
        prices_trades.append({**item[0], **item[1]})
    x = []
    y = []
    for item in prices_trades:
        x.append(item['timestamp'])
        side = -1 if item['side'] == 'S' else 1
        y.append(float(item['lastPrice']) - float(item['price']) * int(item['volume']) * side)
    plt.plot(x, y)
    plt.savefig(output)
    plt.show()


if __name__ == "__main__":
    calc_pnl_and_draw_picture("/tmp/price.csv", "/tmp/trade.csv", "/tmp/pnl.png")
