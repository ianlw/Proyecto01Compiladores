def find_symbols(reglas):
    rules = reglas
    terminals = set()
    non_terminals = set()
    primerSimbolo = '$'
    for non_terminal, productions in rules.items():
        if (primerSimbolo == '$'): primerSimbolo = non_terminal
        non_terminals.add(non_terminal)
        for production in productions:
            for symbol in production.split():
                if not symbol.isupper() and symbol not in ('ε', '|'):
                    terminals.add(symbol)
                elif symbol.isupper():
                    non_terminals.add(symbol)
    return terminals, non_terminals, primerSimbolo

if __name__ == "__main__":
    rules = {
        "E": ["E E'", "T"],
        "E'": ["+ T", "- T"],
        "T": ["F T'"],
        "T'": ["* T", "/ T", "ε"],
        "F": ["( E )", "id", "n"]
    }

    a, b, c = find_symbols(rules)
