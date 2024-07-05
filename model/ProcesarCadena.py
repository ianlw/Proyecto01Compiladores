import matplotlib.pyplot as plt
import pandas as pd

# Definir la función para crear la tabla de análisis
def create_parse_table_image(procedure_steps):
    # Crear un DataFrame a partir de los pasos del procedimiento
    df = pd.DataFrame(procedure_steps, columns=['Pila', 'Cadena', 'Acción'])
    
    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis('tight')
    ax.axis('off')

    # Crear la tabla
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colColours=['#d4e6f1']*3)
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)
    
    # Guardar la imagen
    plt.savefig('./parse_table.png', bbox_inches='tight', pad_inches=0.1)
    plt.close()

# Función de análisis sintáctico modificada
def parse(input_string, parse_table, start_symbol, terminals, non_terminals):
    tokens = input_string.split()
    tokens.append('$')
    stack = ['$', start_symbol]
    index = 0
    procedure_steps = []

    while len(stack) > 0:
        top = stack.pop()
        current_input = tokens[index]
        procedure_steps.append((' '.join(stack[::-1]), ' '.join(tokens[index:]), f"Top: {top}, Input: {current_input}"))

        if top in terminals or top == '$':
            if top == current_input:
                index += 1
                procedure_steps[-1] = (procedure_steps[-1][0], procedure_steps[-1][1], 'Coincide')
            else:
                procedure_steps[-1] = (procedure_steps[-1][0], procedure_steps[-1][1], 'Error')
                create_parse_table_image(procedure_steps)
                return False
        elif top in non_terminals:
            if (top, current_input) in parse_table:
                production = parse_table[(top, current_input)]
                procedure_steps[-1] = (procedure_steps[-1][0], procedure_steps[-1][1], f"{top} -> {' '.join(production)}")
                if production != ['ε']:
                    stack.extend(production[::-1])
            else:
                procedure_steps[-1] = (procedure_steps[-1][0], procedure_steps[-1][1], 'Error')
                create_parse_table_image(procedure_steps)
                return False
        else:
            procedure_steps[-1] = (procedure_steps[-1][0], procedure_steps[-1][1], 'Error')
            create_parse_table_image(procedure_steps)
            return False

        if len(stack) == 0:
            create_parse_table_image(procedure_steps)
            return True

    create_parse_table_image(procedure_steps)
    return False

# Ejemplo de uso
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

test_string = "n + n * n"
result = parse(test_string, parse_table, start_symbol, terminals, non_terminals)
print(f"Cadena: {test_string} -> {result}")
