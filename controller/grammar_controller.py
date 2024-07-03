from model.grammar_recursion_eliminator import eliminar_recursion, eliminar_ambiguedad 
from view.main_window import GrammarView
from model.tabla import crear_tabla 
from Ambiguedad import eliminar_ambiguedad
from Primeros import calcular_conjunto_primero
from Siguientes import calcular_conjunto_siguiente
from model.Terminales import find_symbols
from model.ProcesarCadena import parse

class GrammarController:
    def __init__(self, root):
        self.root = root
        self.view = GrammarView(root, self.procesar_gramatica, self.Procesar_cadena)

    def Procesar_cadena(self):
        input_txtCadena = self.view.input_cadena()
        input_txtGramatica = self.view.input_gramatica()
        
        if not input_txtCadena:
            self.view.mensaje_error("Por favor, ingrese una cadena.")
            return 
        
        if not input_txtGramatica:
            self.view.mensaje_error("Por favor, ingrese una gramática.")
            return 

        try:
            gramatica = self.parse_gramatica(input_txtGramatica)  # Parsear el lenguaje
            no_recursion_gramatica = eliminar_recursion(gramatica)  # Eliminar la recursión
            no_ambiguedad_gramatica = eliminar_ambiguedad(no_recursion_gramatica)  # Eliminar la ambigüedad

            terminales, no_terminales, primer_simbolo = find_symbols(no_ambiguedad_gramatica)
            conjunto_primeros = calcular_conjunto_primero(no_ambiguedad_gramatica)  # Calcular los conjuntos primeros
            conjunto_siguientes = calcular_conjunto_siguiente(no_ambiguedad_gramatica, conjunto_primeros)

            tabla = crear_tabla(no_ambiguedad_gramatica, conjunto_primeros, conjunto_siguientes)

            Verdad = parse(input_txtCadena, tabla, primer_simbolo, terminales, no_terminales)
            self.view.output_cadena(Verdad)
        except Exception as e:
            self.view.mensaje_error(f"Error en la digitación de la cadena: {e}")

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
            print(no_ambiguedad_gramatica)
            print(conjunto_primeros)
            print(conjunto_siguientes)
            tabla = crear_tabla(no_ambiguedad_gramatica, conjunto_primeros, conjunto_siguientes)
            self.view.mostrar_tabla()
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
