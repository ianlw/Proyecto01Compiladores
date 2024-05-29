import re
from collections import defaultdict

def eliminar_recursion(gramatica):
    nueva_gramatica = {}
    for no_terminal, producciones in gramatica.items():
        recursivas = []
        no_recursivas = []
        
        for produccion in producciones:
            if produccion.startswith(no_terminal):
                # Extraer la parte recursiva removiendo el no terminal inicial
                recursivas.append(produccion[len(no_terminal):].strip())
            else:
                no_recursivas.append(produccion.strip())
        
        if recursivas:
            nuevo_no_terminal = no_terminal + "'"
            nueva_gramatica[no_terminal] = [prod + " " + nuevo_no_terminal for prod in no_recursivas]
            nueva_gramatica[nuevo_no_terminal] = [prod + " " + nuevo_no_terminal for prod in recursivas] + ['ε']
        else:
            nueva_gramatica[no_terminal] = producciones
    
    return nueva_gramatica

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

