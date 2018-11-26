'''
Dunder method: is a special method to ensure 'myclass' perform like the inner data model, e.g. the numerical or sequence.
               advantages: 1) don't need class.method() to call for, e.g. deck.__getitem__(0)--> deck[0]
                           2) can use standard library method simply, e.g.  random.choice(deck)
                           3) efficient

    #sequence:
            string:   __repr__(), __str__()
            numerical transform:  __bool__(), __int__(), __float__(), __hash__()
            *set model:   __len__(),
                          __getitem__(), __setitem__()    #  num = s[i], s[i] = num
                          __delitem__()         # del s[i]
                          __contains__()       # in set
                          __index__(v)         # return the index of 'v' in the list
            iterator:     __iter__()
                          __next__()
                          __reversed__()
            call:    __call__()
            context:   __enter__(), __exit__()
            attr:   __getattr__(),  __setattr__(), __delattr__(),  __dir__()

    #numerical:
            operation: __abs__(), __add__() +,  __sub__() -, __truediv__() /, __mul__() *, __floordiv__() //, __mod__() %, __pow__() **
            comparison: __lt__() <, __le__() <=, __eq__() =, __ne__() !=, __gt__() >, __ge__() >=

'''
'''
sequence
'''
from collections import namedtuple
from random import choice

Card = namedtuple('Card',['rank','suit'])

class FrenchDeck():
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for rank in self.ranks
                      for suit in self.suits]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, item):
        return self._card

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# # test
# deck = FrenchDeck()
# print(deck[0], deck[:3], choice(deck))
# for card in sorted(deck, key=suit_values):
#     print(card)


'''
numerical:
'''
from math import hypot

class Vector():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector (%r %r)' % (self.x, self.y)
    __str__= __repr__

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v = Vector(3,4)
v_2 = Vector(1,1)
print(abs(v))
print(v*3)
print(v + v_2)