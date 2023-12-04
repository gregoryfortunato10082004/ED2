# Avalia a árvore binária e retorna o resultado da expressão
def eval_tree(node, vars):
    if node.value in "+-*/":
        left = eval_tree(node.left, vars)
        right = eval_tree(node.right, vars)
        if node.value == '+': return left + right
        if node.value == '-': return left - right
        if node.value == '*': return left * right
        if node.value == '/': return left / right
    elif node.value in vars:
        return vars[node.value]
    else:
        return float(node.value)

     
|# Função principal que lê a expressão do usuário, verifica se os parênteses estão balanceados, constrói a árvore e avalia a expressão
def repl():
    vars = {}
    while True:
        expr = input("> ")
        if expr == "exit": break
        if not check_parentheses(expr):
            print("Erro: parênteses desbalanceados")
            continue
        if "=" in expr:
            var, expr = expr.split("=")
            vars[var.strip()] = eval_tree(build_tree(parse_expr(expr)), vars)
        else:
            print(eval_tree(build_tree(parse_expr(expr)), vars))

repl()