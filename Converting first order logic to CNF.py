def elim_impli(s):
    s = s.replace("<->","=")

    if "->" in s:
        a, b = s.split("->")
        s = f"(~{a.strip()} | {b.strip()})"

    if "=" in s:
        a, b = s.split("=")
        s = f"(({a.strip()} -> {b.strip()}) & ({b.strip()} -> {a.strip()}))"
        s = elim_impli(s)
    return s

def move_nega(s):
    s = s.replace("~~"," ")
    return s

def distri(s):
    if "&" in s and "|" in s:
        parts 
        if len(parts) == 2:
            a, b = parts
            return f"({a.strip()} | {b.strip()})"
        return s

def convert_cnf(formula):
    formula = elim_impli(formula)
    formula = move_nega(formula)
    formula = distri(formula)
    return formula

formula = input("Enter formula: ")
result = convert_cnf(formula)
print("CNF :", result)