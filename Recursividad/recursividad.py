# eliminar_recursion.py

def eliminar_recursion_directa(gramatica):
    nueva_gramatica = {}
    for no_terminal, producciones in gramatica.items():
        recursivas = []
        no_recursivas = []
        
        for produccion in producciones:
            if produccion.startswith(no_terminal):
                recursivas.append(produccion[len(no_terminal):])
            else:
                no_recursivas.append(produccion)
        
        if recursivas:
            nuevo_no_terminal = no_terminal + "'"
            nueva_gramatica[no_terminal] = [prod + nuevo_no_terminal for prod in no_recursivas]
            nueva_gramatica[nuevo_no_terminal] = [prod + nuevo_no_terminal for prod in recursivas] + ['ε']
        else:
            nueva_gramatica[no_terminal] = producciones
    
    return nueva_gramatica
