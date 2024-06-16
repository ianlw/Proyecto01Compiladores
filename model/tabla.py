import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import pandas as pd

class TablaAnalisisSintactico:
    def __init__(self,gramatica, primeros, siguientes) -> None:
        self.gramatica = gramatica
        self.primeros = primeros
        self.siguientes = siguientes

    def construct_ll_table(self, gramatica, primeros, siguientes):
        ll_table = {}
        for non_terminal, productions in gramatica.items():
            for production in productions:
                first_symbol = production[0]
                if first_symbol in primeros:  # Check if it's a non-terminal
                    for terminal in primeros[first_symbol]:
                        ll_table[(non_terminal, terminal)] = production
                elif first_symbol == 'ε':  # Handle epsilon productions
                    for terminal in siguientes[non_terminal]:
                        ll_table[(non_terminal, terminal)] = production
                else:  # It's a terminal
                    ll_table[(non_terminal, first_symbol)] = production
        return ll_table

    # gramatica = {
    #     'E': [('T', "E'")],
    #     "E'": [('+', 'T', "E'"), ('-', 'T', "E'"), ('ε',)],
    #     'T': [('F', "T'")],
    #     "T'": [('*', 'F', "T'"), ('/', 'F', "T'"), ('ε',)],
    #     'F': [('id',), ('n',)]
    # }
    #
    # primeros = {
    #     'E': {'id', 'n'},
    #     "E'": {'+', '-', 'ε'},
    #     'T': {'id', 'n'},
    #     "T'": {'*', '/', 'ε'},
    #     'F': {'id', 'n'}
    # }
    #
    # siguientes = {
    #     'E': {'$'},
    #     "E'": {'$'},
    #     'T': {'$', '+', '-'},
    #     "T'": {'$', '+', '-'},
    #     'F': {'$', '*', '+', '-', '/'}
    # }

    # Constructing the LL table
def crear_tabla(gramatica, primeros, siguientes): 
    table = TablaAnalisisSintactico(gramatica, primeros, siguientes)
    ll_table = table.construct_ll_table(gramatica, primeros, siguientes)

    # Initialize an empty DataFrame for visualization
    df = pd.DataFrame(columns=['Non-Terminal', 'Terminal', 'Production'])

    # Use loc indexer to add rows to the DataFrame
    row_index = 0
    for (non_terminal, terminal), production in ll_table.items():
        df.loc[row_index] = [non_terminal, terminal, ' '.join(production)]
        row_index += 1

    # Pivot the DataFrame to create a double-entry table with non-terminals as rows
    pivot_df = df.pivot(index='Non-Terminal', columns='Terminal', values='Production')

    # Fill NaN values with an empty string for better readability
    pivot_df = pivot_df.fillna('')

    # Plotting using matplotlib
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=pivot_df.values,
             colLabels=pivot_df.columns,
             rowLabels=pivot_df.index,
             cellLoc = 'center', loc='center')


    # Guardar la figura en la ubicación del archivo especificada
    fig.savefig("./tabla_ll.png", bbox_inches='tight')
    
    # Cerrar la figura para liberar memoria
    plt.close(fig)
