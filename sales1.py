#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
from dataclasses import dataclass, field
from functools import reduce
# from typing import List
# cSpell:ignore datefmt

# version of my today's use. I do not fully utilize type checking.


@dataclass
class Order:
    order_number: int
    itemlines: list = field(default_factory=list, init=False)

    def __post_init__(self):
        self.order_number = int(self.order_number)

    @property
    def total_order_qty(self):
        def _do_sum(a, b):
            return a.qty + b.qty
        return reduce(_do_sum, self.itemlines)

    @property
    def total_order_price(self):
        def _do_sum(a, b):
            return a.extended_price + b.extended_price
        return reduce(_do_sum, self.itemlines)


@dataclass
class Itemline:
    itemline_number: int
    item_number: str
    qty: int
    unit_price: float

    @property
    def extended_price(self):
        return self.unit_price * self.qty


def main():
    order1 = Order(order_number=1)
    order1.itemlines.append(
        Itemline(
            itemline_number=10,
            item_number='Vanilla',
            qty=3,
            unit_price=1.00
        )
    )
    order1.itemlines.append(
        Itemline(
            itemline_number=20,
            item_number='Chocolate',
            qty=5,
            unit_price=1.20
        )
    )

    print(f'Total Order Qty: {order1.total_order_qty}.')
    print(f'Total Order Price: {order1.total_order_price}.')


def test():
    pass


if __name__ == '__main__':

    # logger setup
    filename = str(sys.argv[0])[:-3] + '.log'
    format = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)-8s: %(message)s'
    logging.basicConfig(
        filename=filename,
        format=format,
        datefmt='%m-%d %H:%M',
        level=logging.INFO,
        # level   =logging.DEBUG,
        # level   =logging.ERROR,
    )

    # https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    main()
