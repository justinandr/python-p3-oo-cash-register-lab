#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous = []

    def add_item(self, name, price, quantity = 1):
        for _ in range(quantity):
            self.items.append(name)

        self.total += price * quantity
        self.previous.append(
            {"item": name, "quantity": quantity, "price": price}
        )

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f'After the discount, the total comes to ${self.total}.')
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        if not self.previous:
            return "There are no transactions to void."
        self.total -= (
            self.previous[-1]["price"]
            * self.previous[-1]["quantity"]
        )
        for _ in range(self.previous[-1]["quantity"]):
            self.items.pop()
        self.previous.pop()