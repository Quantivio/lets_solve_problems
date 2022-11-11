# Leet Code Problem: Online Stock Span
# Link: https://leetcode.com/problems/online-stock-span/
# Complexity: Medium
# Description: Write a class StockSpanner which collects daily price quotes for some stock, and returns the
# span of that stock's price for the current day.

"""
Example:
    Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
    Output: [null,1,1,1,2,1,4,6]
    Explanation: For 100 there is no previous price, so the span is 1 because 100 is <= 100.
    For 80 there is previous price which is 100 so 100 <= 80 condition will fail but 80 <= 80 so the span is 1.
    For 60 there is previous price which is 60 so 80 <= 80 condition will fail but 60 <= 60 so the span is 1.
    For 70 there is previous price which is 60 so 60 <= 70 condition will pass so the span becomes 1 and
    also 70 <= 70 so the span becomes 2.
    By following this pattern we can find the span for all the prices.
"""

from time import perf_counter


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        "Simple counter technique with for loop. Won't be able to handle large inputs"
        self.stack.append(price)
        count = 0
        if price:
            for stock in self.stack[::-1]:
                if stock <= price:
                    count += 1
                if stock > price:
                    break
        return count

    def next_with_stack(self, price: int) -> int:
        "Using stack to keep track of previous prices and spans"
        current_span = 1

        while self.stack and self.stack[-1][0] <= price:
            current_span += self.stack.pop()[1]
        self.stack.append((price, current_span))
        return current_span


if __name__ == "__main__":
    start = perf_counter()
    stock_spanner = StockSpanner()
    print(stock_spanner.next_with_stack(100))
    print(stock_spanner.next_with_stack(80))
    print(stock_spanner.next_with_stack(60))
    print(stock_spanner.next_with_stack(70))
    print(stock_spanner.next_with_stack(60))
    print(stock_spanner.next_with_stack(75))
    print(stock_spanner.next_with_stack(85))
    end = perf_counter()
    print(f"Time taken with stack: {end - start}")

    start = perf_counter()
    stock_spanner = StockSpanner()
    print(stock_spanner.next(100))
    print(stock_spanner.next(80))
    print(stock_spanner.next(60))
    print(stock_spanner.next(70))
    print(stock_spanner.next(60))
    print(stock_spanner.next(75))
    print(stock_spanner.next(85))
    end = perf_counter()
    print(f"Time taken without stack: {end - start}")
