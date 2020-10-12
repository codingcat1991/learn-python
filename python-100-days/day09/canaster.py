import random


class Card(object):
    """一张牌"""
    __slots__ = ('_suite', '_face')

    def __init__(self, suite, face):
        """初始化方法"""
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)


class Poker(object):
    """一副牌"""
    __slots__ = ('_cards', '_current')

    def __init__(self):
        self._cards = [Card(suite, face) for suite in '♠♥♣♦' for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌（随机乱序）"""
        self._current = 0
        random.shuffle(self._cards)

    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""
    __slots__ = ('_name', '_cards_on_hand',)

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, cark_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=cark_key)


# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return card.suite, card.face


def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next())
    for player in players:
        print('%s : ' % player.name, end=' ')
        player.arrange(get_key)
        for card in player.cards_on_hand:
            print(card.suite, card.face, end=',')
        print()


if __name__ == '__main__':
    main()
