import re
from collections import defaultdict

# Función para parsear la gramática desde una cadena de texto
def parsear_gramatica(entrada):
    gramatica = defaultdict(list)
    lineas = entrada.strip().split('\n')
    for linea in lineas:
        lhs, rhs = linea.split('->')
        lhs = lhs.strip()
        rhs = [alt.strip() for alt in rhs.split('|')]
        gramatica[lhs].extend(rhs)
    print(gramatica)
    return gramatica

# Función para realizar la factorización a la izquierda
def factorizar_izquierda(gramatica):
    nuevas_reglas = defaultdict(list)
    for no_terminal, producciones in gramatica.items():
        mapa_prefijos = defaultdict(list)
        for produccion in producciones:
            primer_simbolo = produccion.split()[0] if produccion.split() else ''
            mapa_prefijos[primer_simbolo].append(produccion)

        for prefijo, prods in mapa_prefijos.items():
            if len(prods) == 1:
                nuevas_reglas[no_terminal].append(prods[0])
            else:
                nuevo_no_terminal = no_terminal + "'"
                nuevas_reglas[no_terminal].append(prefijo + ' ' + nuevo_no_terminal)
                nuevas_reglas[nuevo_no_terminal].extend([prod[len(prefijo):].strip() or 'ε' for prod in prods])
    
    return nuevas_reglas

# Función principal para eliminar la ambigüedad de la gramática
def eliminar_ambiguedad(gramatica):
    gramatica_factorizada = factorizar_izquierda(gramatica)
    return gramatica_factorizada

# Función para imprimir la gramática de manera legible
def imprimir_gramatica(gramatica):
    for no_terminal, producciones in gramatica.items():
        print(f"{no_terminal} -> {' | '.join(producciones)}")

# Función principal del programa
def main():
    entrada = """\
    E -> E + T | E - T | T
    T -> F * T | F / T | F
    F -> (E) | id | n
    """
    
    print("Gramática Original:")
    gramatica = parsear_gramatica(entrada)
    imprimir_gramatica(gramatica)
    
    print("\nDespués de Eliminar la Ambigüedad:")
    gramatica_sin_ambiguedad = eliminar_ambiguedad(gramatica)
    imprimir_gramatica(gramatica_sin_ambiguedad)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
