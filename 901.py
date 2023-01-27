
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        
        self.count = 1

        while self.stack and price >= self.stack[-1][0]:
            popped = self.stack.pop()
            self.count += popped[1]
        
        self.stack.append((price, self.count))

        return self.count