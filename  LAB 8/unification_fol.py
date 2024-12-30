def parse_predicate(predicate):
    name, args = predicate.split('(')
    args = args.rstrip(')').split(', ')
    return name, args

def is_variable(term):
    return term[0].islower()

def unify(x, y, subst={}):
    name1, args1 = parse_predicate(x)
    name2, args2 = parse_predicate(y)
    if name1 != name2 or len(args1) != len(args2):
        return None
    for a, b in zip(args1, args2):
        subst = unify_terms(a, b, subst)
        if subst is None:
            return None
    return subst

def unify_terms(a, b, subst):
    a = apply_substitution(a, subst)
    b = apply_substitution(b, subst)
    if a == b:
        return subst
    if is_variable(a):
        return extend_subst(a, b, subst)
    if is_variable(b):
        return extend_subst(b, a, subst)
    return None

def apply_substitution(term, subst):
    while is_variable(term) and term in subst:
        term = subst[term]
    return term

def extend_subst(var, value, subst):
    if occurs_check(var, value, subst):
        return None
    subst = subst.copy()
    subst[var] = value
    return subst

def occurs_check(var, value, subst):
    if var == value:
        return True
    if is_variable(value) and value in subst:
        return occurs_check(var, subst[value], subst)
    return False

predicate1 = "Parent(x, y)"
predicate2 = "Parent(John, Mary)"
substitution = unify(predicate1, predicate2)

if substitution is not None:
    print("Unification Successful!")
    print("Substitution:", substitution)
else:
    print("Unification Failed.")
