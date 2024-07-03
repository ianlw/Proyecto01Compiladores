import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class TablaAnalisisSintactico:
    def __init__(self, gramatica, primeros, siguientes) -> None:
        self.gramatica = gramatica
        self.primeros = primeros
        self.siguientes = siguientes

    def construct_ll_table(self):
        ll_table = {}
        for non_terminal, productions in self.gramatica.items():
            for production in productions:
                first_symbol = production[0]
                if first_symbol in self.primeros: 
                    for terminal in self.primeros[first_symbol]:
                        ll_table[(non_terminal, terminal)] = production
                elif first_symbol == 'ε':
                    for terminal in self.siguientes[non_terminal]:
                        ll_table[(non_terminal, terminal)] = production
                else: 
                    ll_table[(non_terminal, first_symbol)] = production
        return ll_table

def transformar_gramatica(gramatica):
    nueva_gramatica = {}
    for key, productions in gramatica.items():
        nueva_gramatica[key] = [prod.split() for prod in productions]
    return nueva_gramatica

def crear_tabla(gramatica, primeros, siguientes): 
    gramatica_transformada = transformar_gramatica(gramatica)
    table = TablaAnalisisSintactico(gramatica_transformada, primeros, siguientes)
    ll_table = table.construct_ll_table()

    df = pd.DataFrame(columns=['Non-Terminal', 'Terminal', 'Production'])
    row_index = 0
    for (non_terminal, terminal), production in ll_table.items():
        df.loc[row_index] = [non_terminal, terminal, ' '.join(production)]
        row_index += 1

    pivot_df = df.pivot(index='Non-Terminal', columns='Terminal', values='Production')
    pivot_df = pivot_df.fillna('Error')

    # Aplicar estilo para celdas con "Error"
    def highlight_error(val):
        color = 'red' if val == 'Error' else 'black'
        return f'color: {color}'

    styled_df = pivot_df.style.applymap(highlight_error)

    # Convertir el estilo a una imagen
    fig, ax = plt.subplots(figsize=(9, 3))
    ax.axis('tight')
    ax.axis('off')

    table = ax.table(cellText=pivot_df.values,
                     colLabels=pivot_df.columns,
                     rowLabels=pivot_df.index,
                     cellLoc='center', loc='center')

    # Ajustar el tamaño de la tabla para que las celdas no se amontonen
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2.2)

    # Aplicar colores a las celdas
    for (i, j), val in np.ndenumerate(pivot_df.values):
        if val == 'Error':
            table[i+1, j].set_text_props(color='red')

    # Guardar la tabla como imagen
    fig.savefig("./tabla_ll.png", bbox_inches='tight')

    plt.close(fig)
    return ll_table

# Ejemplo de uso
gramatica = {
    'E': ["T E'"],
    "E'": ["+ T E'", "- T E'", 'ε'],
    'T': ["F T'"],
    "T'": ['* T', '/ T', 'ε'],
    'F': ['( E )', 'id', 'n']
}

primeros = {
    'E': {'id', 'n', '('},
    "E'": {'+', '-', 'ε'},
    'T': {'id', 'n', '('},
    "T'": {'*', '/', 'ε'},
    'F': {'id', 'n', '('}
}

siguientes = {
    'E': {')', '$'},
    "E'": {')', '$'},
    'T': {'$', '-', ')', '+'},
    "T'": {'$', '-', ')', '+'},
    'F': {'$', '*', '+', '/', '-', ')'}
}

a = crear_tabla(gramatica, primeros, siguientes)
print(a)
