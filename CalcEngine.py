class CalcEngine:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def add(self, a):
        self.result += a
        return self.result

    def get_result(self):
        return self.result

    def sub(self, a, b):
        self.result = a - b
        return self.result

    def mul(self, a, b):
        self.result = a * b
        return self.result

    def div(self, a, b):
        self.result = a / b
        return self.result

    def percent(self, a, b):
        self.result = a * b / 100
        return self.result

