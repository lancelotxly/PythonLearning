from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', ['name','fidelity'])

class LineItem():
    def __init__(self,product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order():  # context
    def __init__(self,customer,cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,'_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC): # Abstract strategy
    @abstractmethod
    def discount(self,order):
        '''return the discount(positive)'''

class FidelityPromo(Promotion):  # First embodied strategy
    '''5% discount for the user with 1000 credits'''

    def discount(self,order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):  # Second embodied strategy
    '''10% discount for a commodity which total over 20'''

    def discount(self,order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):  # Thrid embodied strategy
    '''7% discount for the different commodity which total over 10'''

    def discount(self,order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * .07
        return 0