class FollowSets:
    def __init__(self, grammar, first_sets):
        self.grammar = grammar
        self.first_sets = first_sets
        self.non_terminals = list(grammar.keys())
        self.follow_sets = {nt: set() for nt in self.non_terminals}
        self.follow_sets[self.non_terminals[0]].add('$')  # Start symbol
        self.compute_follow_sets()

    def compute_follow_sets(self):
        while True:
            updated = False
            for head in self.grammar:
                for production in self.grammar[head]:
                    trailer = self.follow_sets[head].copy()
                    for symbol in reversed(production.split()):
                        if symbol in self.non_terminals:
                            if trailer - self.follow_sets[symbol]:
                                self.follow_sets[symbol].update(trailer)
                                updated = True
                            if 'ε' in self.first_sets[symbol]:
                                trailer.update(self.first_sets[symbol] - {'ε'})
                            else:
                                trailer = self.first_sets[symbol]
                        else:
                            trailer = self.first_sets.get(symbol, {symbol})
            if not updated:
                break

    def get_follow_sets(self):
        return self.follow_sets

def calcular_conjunto_siguiente(grammar, first_sets):
    parser = FollowSets(grammar, first_sets)
    return parser.get_follow_sets()

if __name__ == "__main__":
    grammar = {
        'E': ['E + T', 'E - T', 'T'],
        'T': ['F * T', 'F / T', 'F'],
        'F': ['( E )', 'id', 'n']
    }

    from Primeros import calcular_conjunto_primero
    first_sets = calcular_conjunto_primero(grammar)
    
    follow_sets = calcular_conjunto_siguiente(grammar, first_sets)
    print("Follow sets:")
    for non_terminal, follow_set in follow_sets.items():
        print(f"FOLLOW({non_terminal}) = {follow_set}")
