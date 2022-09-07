import datetime
import random
import pandas as pd


def generate_data(symbol_list, datetime_start, datetime_end, column_list):
    start = datetime.datetime.strptime(datetime_start, '%Y%m%d %H:%M:%S')
    end = datetime.datetime.strptime(datetime_end, '%Y%m%d %H:%M:%S')
    data = {item: [] for item in column_list}
    data.update({"symbol": [], "time": []})
    while start <= end:
        for key in column_list:
            data[key].append(round(random.random(), 6))
        data["symbol"].append(random.choice(symbol_list))
        data["time"].append(start.strftime('%Y-%m-%d %H:%M:%S'))
        start = start + datetime.timedelta(seconds=1)
    return pd.DataFrame(data)


def cal_min_bar(df):
    df.insert(df.shape[1], 'open', [round(random.random(), 6) for _ in df['time']])
    df.insert(df.shape[1], 'high', [round(random.random(), 6) for _ in df['time']])
    df.insert(df.shape[1], 'low', [round(random.random(), 6) for _ in df['time']])
    df.insert(df.shape[1], 'close', [round(random.random(), 6) for _ in df['time']])
    df.insert(df.shape[1], 'bar_ret', df['close'] / df['open'])
    df.insert(df.shape[1], 'flag', df.apply(lambda x: 1 if x['high'] / x['close'] < 1.5 else 0, axis=1))
    return df


def select_data(df, n):
    data = df[df.flag == 1].sort_values(by=['bar_ret'], ascending=False).head(n)
    return pd.DataFrame(data, columns=['symbol', 'time', 'bar_ret'])


if __name__ == "__main__":
    symbol_list = list("ABC")
    start = "20180103 09:00:00"
    end = "20180103 15:00:00"
    column_list = ["last_price", "ask1", "bid1"]
    price_data = generate_data(symbol_list, start, end, column_list)
    print(price_data)

    bar_data = cal_min_bar(price_data[["time", "symbol", "last_price"]])
    print(bar_data.head())

    focus_data = select_data(bar_data, 3)
    print(focus_data)
