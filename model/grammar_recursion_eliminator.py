from collections import defaultdict

def eliminar_recursion(gramatica):
    # Diccionario para almacenar la nueva gramática
    nueva_gramatica = {}
    
    # Iterar sobre cada no terminal en la gramática
    for no_terminal, producciones in gramatica.items():
        # Listas para almacenar producciones recursivas y no recursivas
        recursivas = []
        no_recursivas = []
        
        # Iterar sobre cada producción para clasificarlas como recursivas o no recursivas
        for produccion in producciones:
            if produccion.startswith(no_terminal):
                # Extraer la parte recursiva removiendo el no terminal inicial
                recursivas.append(produccion[len(no_terminal):].strip())
            else:
                no_recursivas.append(produccion.strip())
        
        # Si hay producciones recursivas
        if recursivas:
            # Crear un nuevo no terminal para las producciones recursivas
            nuevo_no_terminal = no_terminal + "'"
            
            # Crear las nuevas producciones sin recursión
            nueva_gramatica[no_terminal] = [prod + " " + nuevo_no_terminal for prod in no_recursivas]
            
            # Crear las nuevas producciones recursivas y la producción vacía (ε)
            nueva_gramatica[nuevo_no_terminal] = [prod + " " + nuevo_no_terminal for prod in recursivas] + ['ε']
        else:
            # Si no hay producciones recursivas, mantener las producciones originales
            nueva_gramatica[no_terminal] = producciones
    
    return nueva_gramatica

def eliminar_ambiguedad(gramatica):
    # Diccionario para almacenar las nuevas reglas de la gramática sin ambigüedad
    nuevas_reglas = defaultdict(list)
    
    # Iterar sobre cada no terminal en la gramática
    for no_terminal, producciones in gramatica.items():
        # Diccionario para almacenar las producciones según su primer símbolo
        mapa_prefijos = defaultdict(list)
        
        # Clasificar las producciones según su primer símbolo
        for produccion in producciones:
            primer_simbolo = produccion.split()[0] if produccion.split() else ''
            mapa_prefijos[primer_simbolo].append(produccion)

        # Procesar producciones con el mismo primer símbolo
        for prefijo, prods in mapa_prefijos.items():
            if len(prods) == 1:
                # Si solo hay una producción con el mismo prefijo, agregarla directamente
                nuevas_reglas[no_terminal].append(prods[0])
            else:
                # Si hay más de una producción con el mismo prefijo, crear un nuevo no terminal
                nuevo_no_terminal = no_terminal + "'"
                
                # Agregar una nueva regla con el prefijo y el nuevo no terminal
                nuevas_reglas[no_terminal].append(prefijo + ' ' + nuevo_no_terminal)
                
                # Agregar las producciones restantes sin el prefijo
                nuevas_reglas[nuevo_no_terminal].extend([prod[len(prefijo):].strip() or 'ε' for prod in prods])
    
    return nuevas_reglas
