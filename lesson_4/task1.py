# Реализовать структуру данных стэк, который за О(1) выдает минимум в стэке

class MinStack:

    def __init__(self):
        self.items = []

    def push(self, item: int) -> None:
        self.items.insert(0, item)

    def pop(self) -> None:
        self.items.pop(0)

    def top(self) -> int:
        return self.items[0]

    def getMin(self) -> int:
        return min(self.items)
