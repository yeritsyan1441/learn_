import copy
import random

"""1․ Գրել MyList class, որը կունենա գրեթե բոլոր այն մեթոդները
և ֆունկցիոնալությունը, որը ունի list class-ը առանց ժառանգելու։"""


class MyListError(Exception):
    ...


class MyList:

    def __init__(self, *args):
        self.number = list(args)
        self.d = None

    def append(self, num):
        self.number.append(num)

    def pop(self, index=-1):
        return self.number.pop(index)

    def sort(self, reverse=False):
        # if reverse is False:
        #     for j in range(len(self.number)):
        #         for k in range(len(self.number) - j - 1):
        #             if self.number[k] > self.number[k + 1]:
        #                 self.number[k], self.number[k + 1] = self.number[k + 1], self.number[k]
        # else:
        #     for j in range(len(self.number)):
        #         for k in range(len(self.number) - j - 1):
        #             if self.number[k] < self.number[k + 1]:
        #                 self.number[k], self.number[k + 1] = self.number[k + 1], self.number[k]
        self.number.sort(reverse=reverse)

    def extend(self, iterable):
        self.number.extend(iterable)

    def index(self, element):
        for j in range(len(self.number)):
            if self.number[j] == element:
                return j

    def count(self, element):
        counter = 0
        for j in self.number:
            if j == element:
                counter += 1
        return counter

    def remove(self, element):
        self.number.remove(element)

    def insert(self, position, value):
        self.number.insert(position, value)

    def __copy__(self):
        return MyList(*copy.deepcopy(self.number))

    def __str__(self):
        return f"{self.number}"

    def __len__(self):
        return len(self.number)

    def __repr__(self):
        return f"{self.number}"

    def __add__(self, other):
        return MyList(*(self.number + other.number))

    def __getitem__(self, item):
        return self.number[item]

    def __setitem__(self, key, value):
        self.number[key] = value

    def __delitem__(self, key):
        del self.number[key]

    def __mul__(self, other):
        if isinstance(other, int):
            return MyList(*(self.number * other))
        raise MyListError(f"Invalid type of {other}, must be int")

    def __and__(self, other):
        if isinstance(other, MyList):
            new = []
            for i in self.number:
                if i in other.number and i not in new:
                    new.append(i)
            return MyList(*new)
        raise MyListError(f"Invalid type of {other}, must be MyList")

    def __or__(self, other):
        if isinstance(other, MyList):
            new = []
            for i in self.number:
                if i not in new:
                    new.append(i)
            for i in other.number:
                if i not in new:
                    new.append(i)
            return MyList(*new)
        raise MyListError(f"Invalid type of {other}, must be MyList")

    def __xor__(self, other):
        if isinstance(other, MyList):
            new = []
            for i in self.number:
                if i not in new and i not in other.number:
                    new.append(i)
            for i in other.number:
                if i not in new and i not in self.number:
                    new.append(i)
            return MyList(*new)
        raise MyListError(f"Invalid type of {other}, must be MyList")

    def __sub__(self, other):
        if isinstance(other, MyList):
            new = []
            for i in self.number:
                if i not in new and i not in other.number:
                    new.append(i)
            return MyList(*new)
        raise MyListError(f"Invalid type of {other}, must be MyList")

    def sum(self):
        return sum(self.number)

    def prod(self):
        p = 1
        for i in self.number:
            p *= i
        return p

    def max(self):
        return max(self.number)

    def argmax(self):
        return self.index(self.max())

    def argmin(self):
        return self.index(self.min())

    def argsort(self):
        s = sorted(self.number)
        indexes = []
        for i in self.number:
            ind = s.index(i)
            if ind in indexes:
                s[ind] = None
                ind += 1
            indexes.append(ind)
        return MyList(*indexes)

    def min(self):
        return min(self.number)

    def mean(self):
        return self.sum() / len(self)

    def counter(self):
        d = {}
        for i in self.number:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        self.d = d
        return d

    def most_common(self, k=1):
        if self.d is None:
            self.d = self.counter()
        d1 = dict(sorted(self.d.items(), key=lambda x: x[1], reverse=True)[:k])
        return d1

    def reverse(self):
        self.number.reverse()

    def clear(self):
        self.number.clear()


# l1 = MyList(5, 7, 8, -3, -5, 6, 1, 1, 5, 6, 9, 3, -5, 5, 5, 1, 1)
# l2 = MyList(5, 12, 3, 6, -1, -5, 6, 6)  # [-5, -1, 3, 5, 6, 6, 6, 12]
# print(l1)
# print(l2)
# print(l1 - l2)
# print(l1.counter())
# print(l1.most_common(5))
# print(l2.argsort())  # [3, 7, 2, 4, 1, 0, 5, 6]


# # 1
# class A:
#     pass
#
#
# a = A()
# print(a.__class__.__name__)  # output must be “A”


# 2
"""Create a Deck of cards class.
The deck class should use another class, a Card class.
The Deck class should have a deal method to deal a single card from the deck. 
After a card is dealt, it is removed from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K).
"""


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.suit[0]} {self.value}"


class Deck:
    def __init__(self, all=True):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        if not all:
            values = values[4:]
        self.cards = []
        for s in suits:
            for v in values:
                self.cards.append(Card(s, v))
        self.shuffle()

    def __str__(self):
        return f"{self.cards}"

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        cards = []
        for i in range(n):
            cards.append(self.cards.pop())
        return cards


# d = Deck(all=False)
# print(d.deal(6))
# print(d.deal(6))
# print(d.deal(6))
# print(d.deal(1))
# print(d)

