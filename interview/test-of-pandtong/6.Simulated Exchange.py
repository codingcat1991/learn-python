# 6.	Code exercise - Simulated Exchange
#
#   This code exercise is to simulate exchange for matching orders.
#   - When an order is input, an unique order Id is assigned to the order.
#   - Orders are matched in the ordering of price and time priorities.
#   Please finish class Exchange to fulfil the task in main function.

class Exchange:
    def __init__(self):
        pass

    def InputOrder(self, side, volume, price):
        """
        InputOrder receives order, and return assigned order Id.
        :param side: 0 is buy, 1 is sell,-1 means not valid
        :param volume:order's quantity
        :param price:order's prices
        :return: order Id, an integer
        """
        return 0

    def QueryOrderTrade(self, orderId):
        """
        queries order's trade volume and average price.
        :param orderId: assigned order Id
        :return: (order's trade volume, avg_price),tuple
        """
        return (0, 0.0)


if __name__ == "__main__":
    ex = Exchange()
    orders = list()

    orders.append(ex.InputOrder(0, 1, 100))
    orders.append(ex.InputOrder(0, 2, 101))
    orders.append(ex.InputOrder(0, 3, 102))
    orders.append(ex.InputOrder(1, 4, 100))
    orders.append(ex.InputOrder(1, 5, 101))
    orders.append(ex.InputOrder(1, 6, 102))

    for orderId in orders:
        tradeVolume, avgPrice = ex.QueryOrderTrade(orderId)
        print("orderId:%d,tradeVolume:%d,averagePrcies:%f" % (orderId, tradeVolume, avgPrice))
