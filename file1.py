import argparse
import sys

# Parsing of the arguments of a command line
parser = argparse.ArgumentParser(description='Pure-python command-line calculator.')
parser.add_argument('-m', '--use-modules', metavar='MODULE', dest='module', help='additional modules to use', nargs='+')
parser.add_argument('EXPRESSION', help='expression string to evaluate')
arg = parser.parse_args()
module = arg.module
expr = arg.EXPRESSION

# Printing the results of the parsing of the arguments of a command line
# print("The expression to calculate: {}".format(expr))
# print("The list of the modules' paths to include: {}".format(module))

# Necessary variables
masOfNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', '.']  # the list of numbers
masOfSigns = ['+', '-', '*', '/', '%', '>', '<', '=', '^', '!', '**']
listA = ['<', '>', '=', '!', '*', '/']
OPERATORS = ({
    '+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
    '^': (2, lambda x, y: x ** y), '**': (2, lambda x, y: x ** y),
    '//': (2, lambda x, y: x // y), '%': (2, lambda x, y: x % y),
})
countO = 0  
countC = 0 
i = 0
j = 0
k = 0
y = 0
mas = []
tr = ['+', '-', '%', '^', '*']
h = 0
mas2 = []
stack2 = []

# Some necessary checks for the expression to calculate
if expr is False:
    print("ERROR: the expression to calculate is empty")
    sys.exit()

if len(expr) == 1 and expr[0] == " ":
    print("ERROR: the expression to calculate consists of only a space")
    sys.exit()

while i != len(expr):
    if expr[i] == " ":
        i = i + 1
        if (i == len(expr) - 1) and expr[i] == " ":
            print("ERROR: the expression to calculate consists of only spaces")
            sys.exit()
    else:
        break

if len(expr) == 1 and expr[0] in masOfSigns:
    print("ERROR: the expression to calculate consists of only a sign")
    sys.exit()

i = 0
while i != len(expr):
    if expr[i] in masOfSigns or expr[i] == " ":
        i = i + 1
        if i == len(expr) - 1 and expr[i] in masOfSigns:
            print("ERROR: the expression to calculate consists of only signs")
            sys.exit()
        if i == len(expr) - 1 and expr[i] == " ":
            print("ERROR: the expression to calculate consists of only signs or signs and spaces")
            sys.exit()
    else:
        break

if len(expr) == 1 and expr[0] in masOfNumbers:
    print("ERROR: the expression to calculate consists of only a number")
    sys.exit()

i = 0
while i != len(expr):
    if expr[i] in masOfNumbers or expr[i] == " ":
        i = i + 1
        if i == len(expr) - 1 and expr[i] in masOfNumbers:
            print("ERROR: the expression to calculate consists of only numbers")
            sys.exit()
        if i == len(expr) - 1 and expr[i] == " ":
            print("ERROR: the expression to calculate consists of only numbers or numbers and spaces")
            sys.exit()
    else:
        break

# The count of open brackets
i = 0
for i in expr:
    if i == '(':
        countO = countO + 1

# The count of close brackets
i = 0
for i in expr:
    if i == ')':
        countC = countC + 1

if countO != countC:
    print("ERROR: the brackets are not balanced in the expression to calculate")
    sys.exit()

exprInList = list(expr)
parsedExpr = []
number = ''
bracket = ''
sign=''
for s in exprInList:
    if s in masOfNumbers:
        if sign != "":
            parsedExpr.append(sign)
            sign = ''
        number = number + s
    elif s in masOfSigns:
        if number == "":
            sign = sign + s
        else:
            parsedExpr.append(number)
            number = ''
            sign = sign + s
    elif s == '(' or s == ')':
        if number == "":
            bracket = s
            parsedExpr.append(bracket)
            bracket = ''
        else:
            parsedExpr.append(number)
            number = ''
            bracket = s
            parsedExpr.append(bracket)
            bracket = ''
    else:
        print("ERROR: maybe it is a function or something else, but I don't know this now...Sorry")
        sys.exit()

if number:
    parsedExpr.append(number)

stack = []
for token in parsedExpr:
    if token in OPERATORS:
        if stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
            while stack:
                mas.append(stack[-1])
                stack.pop()
            stack.append(token)
        else:
            stack.append(token)
    elif token == "(":
        stack.append(token)
    elif token == ")":
        while stack:
            x = stack.pop()
            if x == "(":
                while stack:
                    mas.append(stack[-1])
                    stack.pop()
                break
            mas.append(x)
    else:
        mas.append(token)

if stack:
    while stack:
        mas.append(stack[-1])
        stack.pop()

while h != len(mas):
    if mas[h] in masOfSigns:
        mas2.append(mas[h])
        h = h+1
    else:
        mas2.append(float(mas[h]))
        h = h+1

for token in mas2:
    if token in OPERATORS:
        y, x = stack.pop(), stack.pop()
        stack.append(OPERATORS[token][1](x, y))
    else:
        stack.append(token)
print(stack[0])


