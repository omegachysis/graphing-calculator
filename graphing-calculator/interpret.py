
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
            if expression[i-1] == "*":
                newExpression += "-1*"
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

    ## turn the whole expression into a large quantity
    #expression = "(" + expression + ")"

    # match starting and closing parantheses
    leftParens = expression.count("(")
    rightParens = expression.count(")")
    expression = expression + ")" * (leftParens - rightParens)

    return expression

def parseExpression(expression, preprocess=True):
    """
    Preprocess expression and convert it
    into Elements.
    """
    if preprocess:
        expression = preprocessExpression(expression)

    elems = []

    mode = None
    value = ""
    quantityLayer = 0
    for i,char in enumerate(expression+"\n"):
        if mode == "Number":
            if char in string.digits + "." + "-":
                value += char
                mode = "Number"
            else:
                elems.append(elements.Number(value))
                mode = None
        elif mode == "Quantity":
            if char == ")":
                if quantityLayer > 0:
                    quantityLayer -= 1
                else:
                    print("QUANTITY PARSE INPUT: ", value)
                    parseValue = parseExpression(value, False)
                    print("QUANTITY PARSE: ", parseValue)
                    elems.append(parseValue)
                    mode = None

            else:
                if char == "(":
                    quantityLayer += 1
                value += char
                mode = "Quantity"

        if mode == None:
            value = ""
            if char in string.digits + "." + "-":
                mode = "Number"
                value += char
            elif char in ["*", "+", "/"]:
                elems.append(elements.Operator(char))
                mode = None
            elif char in string.ascii_letters:
                elems.append(elements.Variable(char))
                mode = None
            elif char == "(":
                mode = "Quantity"
                quantityLayer = 0

    # look for division operators
    # we can turn all of those operators into working fractions
    newElems = []

    skip = 0
    for i,elem in enumerate(elems):
        if skip == 0:
            if isinstance(elem, elements.Operator) and elem.symbol == "/":
                numerator = elems[i-1]
                denominator = elems[i+1]
                newElems.pop()
                newElems.append(elements.Fraction(numerator, denominator))
                skip += 1
            else:
                newElems.append(elem)
        else:
            skip -= 1

    elems = list(newElems)

    return elements.Quantity(elems)

def _test():
    testExpression = "9*(1+2)"
    print(testExpression)
    test = parseExpression(testExpression)
    print(test.elems)
    print(test.express())

    print("Tests succeeded!")