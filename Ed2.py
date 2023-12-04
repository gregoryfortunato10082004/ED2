import re
import operator as op

# Classe para representar um nó em uma árvore binária
class Node:
    def _init_(self, value):
        self.value = value
        self.left = self.right = None

# Verifica se o número de parênteses abertos é igual ao número de parênteses fechados
def check_parentheses(expr):
    return expr.count('(') == expr.count(')')

# Converte a expressão em notação infixa para notação pós-fixa (também conhecida como notação polonesa reversa)
def parse_expr(expr):
    tokens = re.findall("[\d.]+|[\w]+|[+/*()-]", expr)
    prec = {'+':1, '-':1, '*':2, '/':2}
    ops = []
    output = []
    for token in tokens:
        if token in prec:
            while ops and ops[-1] != "(" and prec[token] <= prec[ops[-1]]:
                output.append(ops.pop())
            ops.append(token)
        elif token == "(":
            ops.append(token)
        elif token == ")":
            while ops and ops[-1] != "(":
                output.append(ops.pop())
            ops.pop()
        else:
            output.append(token)
    while ops:
        output.append(ops.pop())
    return output

# Constrói uma árvore binária a partir da expressão em notação pós-fixa
def build_tree(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            node = Node(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            stack.append(Node(token))
    return stack[0]