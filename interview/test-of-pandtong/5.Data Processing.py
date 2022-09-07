# 5.	Code exercise – Data Processing
"""
given symbol_list,like ["A","B"，"C"]
given datetime_start,like "20180103 09:00:00"
given datetime_end,like "20180103 15:00:00"
given column_list,like ["last_price", "ask1", "bid1"]

generate random price in column list for every symbol
from datetime start to datetime end sample every second

       last_price      ask1      bid1 symbol                time
0        0.173368  0.666229  0.650586      A 2018-01-03 09:00:00
1        0.434612  0.771833  0.891474      A 2018-01-03 09:00:01
2        0.222062  0.891160  0.299797      A 2018-01-03 09:00:02
3        0.947866  0.073749  0.169601      A 2018-01-03 09:00:03
4        0.800996  0.548314  0.360005      A 2018-01-03 09:00:04
5        0.529903  0.542695  0.876590      A 2018-01-03 09:00:05

"""


def generate_data(symbol_list, datetime_start, datetime_end, column_list):
    pass


"""
resample the last price column in second to generate open high low close in minutes
generate bar return (bar_ret) column which means close /open
generate flag column: if high / close <1.5 flag=1 else flag = 0
no for loop statement 
                          open      high       low     close    bar_ret  flag
symbol time                                                                        
A 2018-01-03 09:01:00  0.256674  0.996918  0.010180  0.082958   0.323205     0
  2018-01-03 09:02:00  0.114607  0.984437  0.033200  0.409413   3.572324     0
  2018-01-03 09:03:00  0.261541  0.980200  0.002990  0.462317   1.767662     0
  2018-01-03 09:04:00  0.379665  0.949153  0.006085  0.594945   1.567028     0
  2018-01-03 09:05:00  0.029332  0.987624  0.001219  0.314411  10.718877     0
"""


def cal_min_bar(df):
    pass


"""
select every symbol top n bar_ret in subset with condition flag ==1,
no for loop statement 

     symbol                time      bar_ret
19        A 2018-01-03 09:20:00  1165.155037
112       A 2018-01-03 10:53:00   110.638160
211       A 2018-01-03 12:32:00    32.071124
653       B 2018-01-03 13:53:00  1059.186040
377       B 2018-01-03 09:17:00   238.020314
466       B 2018-01-03 10:46:00    66.322434
855       C 2018-01-03 11:14:00    90.620752
1071      C 2018-01-03 14:50:00    47.786062
786       C 2018-01-03 10:05:00    29.567013
"""


def select_data(df, n):
    pass


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
