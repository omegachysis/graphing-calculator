
import elements
import string

def preprocessExpression(expression):
    """
    Process the beginnings of an expression to a form
    that is easier for the computer to interpret.
    """
    expression = str(expression)

    # remove all whitespace
    expression = expression.replace(" ", "")

    # remove all subtraction operators by replacing them with the following formula:
    #  -5 - 4  -->  +-1*5+-1*4
    newExpression = ""
    for i, char in enumerate(expression):
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
    for i, char in enumerate(expression):
        if char != "/":
            newExpression += char
        else:
            newExpression += "*1/"
    expression = newExpression

    # turn the whole expression into a large quantity
    expression = "(" + expression + ")"

    # match starting and closing parantheses
    leftParens = expression.count("(")
    rightParens = expression.count(")")
    expression = expression + ")" * (leftParens - rightParens)

    return expression

def parseExpression(expression):
    """
    Preprocess expression and convert it
    into Elements.
    """
    expression = preprocessExpression(expression)

    elems = []

    mode = None
    value = ""
    for i,char in enumerate(expression):
        if mode == "Number":
            if char in string.digits + "." + "-":
                value += char
            else:
                elems.append(elements.Number(value))
                mode = None

        if mode == None:
            if char in string.digits + "." + "-":
                mode = "Number"
                value += char
            elif char in ["*", "+", "/"]:
                elems.append(elements.Operator(char))
            elif char in string.ascii_letters:
                elems.append(elements.Variable(char))

    print(elems)

    ## search for parentheses
    #for i, char in enumerate(expression):
    #    if char == "(":
    #        minIndex = int(i)
    #        # search backwards for the cooresponding parenthesis
    #        for e, echar in enumerate(reversed(expression)):
    #            if echar == ")":
    #                maxIndex = int(e)
    #        # replace that expression section with a quantity
    #        elems = [expression[:minIndex]

def _test():
    test = preprocessExpression("5 - 4 * 8 + 90")
    assert test == "(5+-1*4*8+90)", "test failed: %s"%repr(test)
    test = preprocessExpression("-9 * 50 - 100 / 5")
    assert test == "(-1*9*50+-1*100*1/5)", "test failed: %s"%repr(test)

    test = parseExpression("-5 * 8")

    print("Tests succeeded!")