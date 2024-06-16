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
                if first_symbol in primeros: 
                    for terminal in primeros[first_symbol]:
                        ll_table[(non_terminal, terminal)] = production
                elif first_symbol == 'ε':
                    for terminal in siguientes[non_terminal]:
                        ll_table[(non_terminal, terminal)] = production
                else: 
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

def crear_tabla(gramatica, primeros, siguientes): 
    table = TablaAnalisisSintactico(gramatica, primeros, siguientes)
    ll_table = table.construct_ll_table(gramatica, primeros, siguientes)

    df = pd.DataFrame(columns=['Non-Terminal', 'Terminal', 'Production'])
    row_index = 0
    for (non_terminal, terminal), production in ll_table.items():
        df.loc[row_index] = [non_terminal, terminal, ' '.join(production)]
        row_index += 1

    pivot_df = df.pivot(index='Non-Terminal', columns='Terminal', values='Production')
    pivot_df = pivot_df.fillna('')

    fig, ax = plt.subplots(figsize=(9, 2))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=pivot_df.values,
             colLabels=pivot_df.columns,
             rowLabels=pivot_df.index,
             cellLoc = 'center', loc='center')


    # Guardar la tabla
    fig.savefig("./tabla_ll.png", bbox_inches='tight')
    
    plt.close(fig)
