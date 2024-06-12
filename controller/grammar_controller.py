from model.grammar_recursion_eliminator import eliminar_recursion, eliminar_ambiguedad 
from view.main_window import GrammarView
from Ambiguedad import eliminar_ambiguedad
from Primeros import calcular_conjunto_primero
from Siguientes import calcular_conjunto_siguiente

class GrammarController:
    def __init__(self, root):
        self.root = root
        self.view = GrammarView(root, self.procesar_gramatica)

    def procesar_gramatica(self):
        input_text = self.view.input_gramatica()
        if not input_text:
            self.view.mensaje_error("Por favor, ingrese una gramática.")
            return
        
        try:
            gramatica = self.parse_gramatica(input_text) #Parsear el lenguaje
            no_recursion_gramatica = eliminar_recursion(gramatica) #Eliminar la recursion
            no_ambiguedad_gramatica = eliminar_ambiguedad(no_recursion_gramatica) #Eliminar la ambiguiedad
            self.view.output_gramatica(no_ambiguedad_gramatica) #Mostrar la gramatica sin recursion ni ambiguedad
            conjunto_primeros = calcular_conjunto_primero(no_ambiguedad_gramatica) #Calcular los conjuntos primeros
            self.view.output_Primeros(conjunto_primeros) #Mostrar los conjuntos primeros
            conjunto_siguientes = calcular_conjunto_siguiente(no_ambiguedad_gramatica, conjunto_primeros)
            self.view.output_Siguientes(conjunto_siguientes)
        except:
            self.view.mensaje_error("Error en la digitación de la gramática")

    def parse_gramatica(self, input_text):
        gramatica = {}
        for line in input_text.splitlines():
            no_terminal, producciones = line.split("->")
            no_terminal = no_terminal.strip()
            producciones = [p.strip() for p in producciones.split('|')]
            gramatica[no_terminal] = producciones
        return gramatica
