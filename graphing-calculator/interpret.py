
def preprocessExpression(expression):
    """
    Process the beginnings of an expression to a form
    that is easier for the computer to interpret.
    """
    expression = str(expression)

    # turn the whole expression into a large quantity
    expression = "(" + expression + ")"

    # remove all whitespace
    expression = expression.replace(" ", "")

    # remove all subtraction operators by replacing them with the following formula:
    #  -5 - 4  -->  +-1*5+-1*4
    newExpression = ""
    for i in range(len(expression)):
        char = expression[i]
        if char != "-":
            newExpression += char
        else:
            newExpression += "+" + "-1*"
    expression = newExpression

    # remove any beginning addition operators
    if expression[0] == "+":
        expression = expression[1:]

    # turn all division operators into multiplication of fractions
    newExpression = ""
    for i in range(len(expression)):
        char = expression[i]
        if char != "/":
            newExpression += char
        else:
            newExpression += "*1/"
    expression = newExpression

    return expression

def _test():
    test = preprocessExpression("5 - 4 * 8 + 90")
    assert test == "(5+-1*4*8+90)", "test failed: %s"%repr(test)