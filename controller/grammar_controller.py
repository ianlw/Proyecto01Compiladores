from model.grammar_recursion_eliminator import eliminar_recursion, eliminar_ambiguedad 
from view.main_window import GrammarView
from Ambiguedad import eliminar_ambiguedad

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
            gramatica = self.parse_gramatica(input_text)
            no_recursion_gramatica = eliminar_recursion(gramatica)
            no_ambiguedad_gramatica = eliminar_ambiguedad(no_recursion_gramatica)
            self.view.output_gramatica(no_ambiguedad_gramatica)
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
