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
