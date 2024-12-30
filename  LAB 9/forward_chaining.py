def forward_chaining_fol(kb, facts, query):
    inferred = set(facts)
    while True:
        new_inferences = set()
        for premises, conclusion in kb:
            if premises.issubset(inferred) and conclusion not in inferred:
                new_inferences.add(conclusion)
        if query in new_inferences:
            return True
        if not new_inferences:
            break
        inferred.update(new_inferences)
    return query in inferred

knowledge_base = [
    ({"Human(John)"}, "Mortal(John)"),
    ({"Parent(John, Mary)", "Human(Mary)"}, "Human(John)"),
    ({"Father(John, Mary)"}, "Parent(John, Mary)"),
    ({"Human(Mary)"}, "Human(John)")
]

facts = {"Father(John, Mary)", "Human(Mary)"}
query = "Mortal(John)"

result = forward_chaining_fol(knowledge_base, facts, query)
print("Query Result:", "Proved" if result else "Not Proved")
