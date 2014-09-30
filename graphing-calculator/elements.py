
class Number(object):
    pass

class Variable(object):
    pass

class Operator(object):
    pass

class Quantity(object):
    expression = ""
    def __init__(self, expression):
        self.expression = expression