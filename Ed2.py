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