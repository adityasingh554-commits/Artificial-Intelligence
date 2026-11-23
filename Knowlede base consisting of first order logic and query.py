def forward_chaining(facts, rules, query):
    if query in facts:
        return True

    while True:
        new_facts = []

        for premisis, conclusion in rules:
            if all(p in facts for p in premisis):

                if conclusion not in facts and conclusion not in new_facts:
                    new_facts.append(conclusion)

                    if conclusion == query:
                        return True

        if not new_facts:
            break

        facts.extend(new_facts)
    return False

facts = ["A","B"]

rules = [
    (["A","B"], "C"),
    (["C"], "D"),
    (["D"],"E")
]

query = input("Enter query: ")

if forward_chaining(facts,rules, query):
    print("True")
else:
    print("False")