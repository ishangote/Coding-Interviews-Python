import unittest
import heapq


class StockPrice:
    def __init__(self):
        self.prices = {}
        self.current_timestamp = -1

    def current(self) -> int:
        return self.prices[self.current_timestamp]

    def update(self, timestamp: int, price: int) -> None:
        pass

    def maximum(self) -> int:
        

    def minimum(self) -> int:
        pass
