class FirstSets:
    def __init__(self, grammar):
        self.grammar = grammar
        self.non_terminals = list(grammar.keys())
        self.terminals = self.get_terminals()
        self.first_sets = {nt: set() for nt in self.non_terminals}
        self.compute_first_sets()

    def get_terminals(self):
        terminals = set()
        for head in self.grammar:
            for production in self.grammar[head]:
                for symbol in production.split():
                    if symbol not in self.non_terminals and not symbol.isupper():
                        terminals.add(symbol)
        return list(terminals)

    def compute_first_sets(self):
        for nt in self.non_terminals:
            self.first(nt)

    def first(self, symbol):
        if symbol in self.terminals:
            return {symbol}
        if symbol not in self.non_terminals:
            return set()
        if 'ε' in self.first_sets[symbol]:
            return self.first_sets[symbol]
        
        for production in self.grammar[symbol]:
            for char in production.split():
                if char == symbol:
                    continue
                char_first_set = self.first(char)
                self.first_sets[symbol].update(char_first_set - {'ε'})
                if 'ε' not in char_first_set:
                    break
            else:
                self.first_sets[symbol].add('ε')
        
        return self.first_sets[symbol]

    def get_first_sets(self):
        return self.first_sets

def calcular_conjunto_primero(grammar):
    parser = FirstSets(grammar)
    return parser.get_first_sets()

if __name__ == "__main__":
    grammar = {
        'E': ['E + T', 'E - T', 'T'],
        'T': ['F * T', 'F / T', 'F'],
        'F': ['( E )', 'id', 'n']
    }
    
    first_sets = calcular_conjunto_primero(grammar)
    print("First sets:")
    for non_terminal, first_set in first_sets.items():
        print(f"FIRST({non_terminal}) = {first_set}")
