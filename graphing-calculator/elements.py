
class Number(object):
    expression = ""
    def __init__(self, expression):
        self.expression = expression

class Variable(object):
    pass

class Operator(object):
    symbol = ""
    def __init__(self, symbol):
        self.symbol = symbol

class Quantity(object):
    expression = ""
    def __init__(self, expression):
        self.expression = expression