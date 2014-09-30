
class Number(object):
    expression = ""
    def __init__(self, expression):
        self.expression = expression
    def express(self):
        return str(self.expression)

class Variable(object):
    pass

class Fraction(object):
    numerator = ""
    denominator = ""
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def express(self):
        expression = "[("
        expression += self.numerator.express()
        expression += ")/("
        expression += self.denominator.express()
        expression += ")]"
        return expression

class Operator(object):
    symbol = ""
    def __init__(self, symbol):
        self.symbol = symbol
    def express(self):
        return str(self.symbol)

class Quantity(object):
    elems = []
    def __init__(self, elems):
        self.elems = elems
    def express(self):
        expression = "("
        for element in self.elems:
            expression += element.express()
        expression += ")"
        return expression
