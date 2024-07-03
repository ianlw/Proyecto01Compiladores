def parse(input_string, parse_table, start_symbol, terminals, non_terminals):
    # Dividir la cadena de entrada en tokens basados en espacios
    tokens = input_string.split()
    tokens.append('$')
    stack = ['$', start_symbol]
    index = 0

    while len(stack) > 0:
        top = stack.pop()
        current_input = tokens[index]

        if top in terminals or top == '$':
            if top == current_input:
                index += 1
            else:
                return False
        elif top in non_terminals:
            if (top, current_input) in parse_table:
                production = parse_table[(top, current_input)]
                #print(f"Applying production: {production}")
                if production != ['ε']:
                    stack.extend(production[::-1])
            else:
                return False
        else:
            return False

        # Check if the input string is fully parsed and the stack is empty
        if len(stack) == 0:
            return True

    return False

# Ejemplo de uso
if __name__ == "__main__":
    parse_table = {
        ('E', 'n'): ['T', "E'"],
        ('E', '('): ['T', "E'"],
        ('E', 'id'): ['T', "E'"],
        ("E'", '+'): ['+', 'T', "E'"],
        ("E'", '-'): ['-', 'T', "E'"],
        ("E'", ')'): ['ε'],
        ("E'", '$'): ['ε'],
        ('T', 'n'): ['F', "T'"],
        ('T', '('): ['F', "T'"],
        ('T', 'id'): ['F', "T'"],
        ("T'", '*'): ['*', 'F', "T'"],
        ("T'", '/'): ['/', 'F', "T'"],
        ("T'", ')'): ['ε'],
        ("T'", '$'): ['ε'],
        ("T'", '-'): ['ε'],
        ("T'", '+'): ['ε'],
        ('F', '('): ['(', 'E', ')'],
        ('F', 'id'): ['id'],
        ('F', 'n'): ['n']
    }

    start_symbol = 'E'
    terminals = ['n', '+', '-', '*', '/', '(', ')', 'id', '$']
    non_terminals = ['E', "E'", 'T', "T'", 'F']

    test_strings = ["n + n", 'id * id', 'n * ( n + n )', 'id + n * id', 'id id']

    for string in test_strings:
        result = parse(string, parse_table, start_symbol, terminals, non_terminals)
        print(f"Cadena: {string} -> {result}")