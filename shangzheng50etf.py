# 投资策略
# 计划每月投入1000，投入10年，总共投入120000，投入
# 0. 资金池：每月1日增加1000
# 1. 底舱：5000<20%*总金额<20000
# 2. 买入规则：买入价格：较上次买入亏损10%买入，买入量：<=1000股
# 3. 卖出规则：上次买入收益达到10%则卖出，卖出量：上次买入量，卖出后底仓不能少于20%*总金额
import akshare as ak
from collections import deque

# 20131101-20231101日k数据
symbol = '510050'
start_date = '20131101'
end_date = '20231101'
hist = ak.fund_etf_hist_em(symbol=symbol, start_date=start_date, end_date=end_date)[['日期', '开盘', '收盘']]
print(hist)
action = {
    'cur_date': None,  # 日期
    'price': None,  # 当前价格
    'action': 'buy',  # 操作, buy/sell
    'quantity': 0,  # 操作数量(股)
    'balance': 0,  # 可用金额
    'total': 0,  # 总投入
    'assets': 0  # 总资产
}

action_records = []
q = deque()


def calc_buy_quantity(price, balance):
    """
    计算买入量，最低买入100股，最多买入1000股，
    :param price: 价格
    :param balance: 可用金额
    :return:
    """
    quantity = balance / price
    quantity = quantity if quantity < 1000 else 1000
    return 0 if quantity < 100 else quantity


def calc_balance(old_balance, price, quantity):
    """
    计算当前余额
    :param old_balance:
    :param price:
    :param quantity:
    :return:
    """
    return old_balance - price * quantity


for row in hist.iterrows():
    tmp_date, tmp_price = row[0], (row[1] + row[2]) / 2
    if int(tmp_date.split('-')[-1]) == 1:
        action['total'] += 1000
        action['balance'] += 1000
    if tmp_date == '2013-11-01':
        quantity = calc_buy_quantity(tmp_price, action['balance'])
        action.update({
            'cur_date': tmp_date,
            'price': tmp_price,
            'action': 'buy',
            'quantity': quantity,
            'balance': calc_balance(action['balance'], tmp_price, quantity),
        })
        action_records.append(action)
        q.append(action)
    else:
        balance = calc_balance(action['balance'], tmp_price, quantity)
        quantity = calc_buy_quantity(tmp_price, balance)
        if tmp_price - action['price'] < -0.1 and quantity > 0:
            print('buy')
            action.update({
                'cur_date': tmp_date,
                'price': tmp_price,
                'action': 'buy',
                'quantity': quantity,
                'balance': calc_balance(action['balance'], tmp_price, quantity),
            })
            action_records.append(action)
            q.append(action)
        if tmp_price - action['price'] > 0.1:
            print('sell')
            tmp_action = q.pop()
            tmp_action.update({
                'cur_date': tmp_date,  # 日期
                'price': action['price'],  # 卖出价格
                'action': action,  # 买入
                'quantity': quantity,  # 买入量
                'balance': balance,  # 可用余额
            })
            action_records.append(tmp_action)
