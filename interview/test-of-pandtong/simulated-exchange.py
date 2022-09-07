class Exchange:
    __ORDER_ID = 0

    def __init__(self):
        self.orders = []

    def InputOrder(self, side, volume, price):
        """
        InputOrder receives order, and return assigned order Id.
        :param side: 0 is buy, 1 is sell,-1 means not valid
        :param volume:order's quantity
        :param price:order's prices
        :return: order Id, an integer
        """
        order_id = Exchange.__ORDER_ID
        self.orders.append({'order_id': order_id, 'side': side, 'volume': volume, 'price': price})
        return Exchange.__ORDER_ID - 1

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
