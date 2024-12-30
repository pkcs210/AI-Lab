def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def IMPLIES(a, b):
    return (not a) or b

def infix_to_postfix(expr):
    precedence = {'NOT': 3, 'AND': 2, 'OR': 2, 'IMPLIES': 1}
    output = []
    stack = []
    tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token not in precedence and token not in {'(', ')'}:
            output.append(token)
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())

    return ' '.join(output)

def eval_postfix(postfix_expr, assignment):
    tokens = postfix_expr.split()
    stack = []
    for token in tokens:
        if token == 'NOT':
            a = stack.pop()
            stack.append(NOT(a))
        elif token in {'AND', 'OR', 'IMPLIES'}:
            b = stack.pop()
            a = stack.pop()
            if token == 'AND':
                stack.append(AND(a, b))
            elif token == 'OR':
                stack.append(OR(a, b))
            elif token == 'IMPLIES':
                stack.append(IMPLIES(a, b))
        else:
            stack.append(assignment.get(token, False))
    return stack.pop()

def generate_assignments(propositions):
    n = len(propositions)
    for i in range(2**n):
        assignment = {}
        for j, prop in enumerate(propositions):
            assignment[prop] = (i & (1 << j)) != 0
        yield assignment

def entails(kb, query, propositions):
    kb_postfix = [infix_to_postfix(sentence) for sentence in kb]
    query_postfix = infix_to_postfix(query)

    for assignment in generate_assignments(propositions):
        kb_true = all(eval_postfix(sentence, assignment) for sentence in kb_postfix)
        if kb_true and not eval_postfix(query_postfix, assignment):
            return False
    return True

if __name__ == "__main__":
    knowledge_base = [
        "A IMPLIES B",
        "B IMPLIES C",
        "A"
    ]
    query = "C"
    propositions = set()
    for sentence in knowledge_base + [query]:
        tokens = sentence.replace('(', ' ').replace(')', ' ').split()
        for token in tokens:
            if token not in {'AND', 'OR', 'NOT', 'IMPLIES'} and token.strip():
                propositions.add(token)
    result = entails(knowledge_base, query, sorted(propositions))
    print("KB entails Query:", "Yes" if result else "No")
