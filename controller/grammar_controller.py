from model.grammar_recursion_eliminator import eliminar_recursion_directa
from view.main_window import GrammarView
from Ambiguedad import eliminar_ambiguedad

class GrammarController:
    def __init__(self, root):
        self.root = root
        self.view = GrammarView(root, self.process_grammar)

    def process_grammar(self):
        input_text = self.view.get_grammar_input()
        if not input_text:
            self.view.show_error_message("Por favor, ingrese una gramática.")
            return
        
        try:
            gramatica = self.parse_grammar(input_text)
            nueva_gramatica = eliminar_recursion_directa(gramatica)
            coregida_gramatica = eliminar_ambiguedad(nueva_gramatica)
            self.view.display_grammar_output(coregida_gramatica)
        except Exception as e:
            self.view.show_error_message(str(e))

    def parse_grammar(self, input_text):
        gramatica = {}
        for line in input_text.splitlines():
            no_terminal, producciones = line.split("->")
            no_terminal = no_terminal.strip()
            producciones = [p.strip() for p in producciones.split('|')]
            gramatica[no_terminal] = producciones
        return gramatica

