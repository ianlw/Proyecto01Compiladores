# grammar_app.py

import tkinter as tk
from tkinter import ttk, messagebox
from recursividad import * 

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Eliminación de Recursión en GLC")

        self.create_widgets()

    def create_widgets(self):
        # Entrada de gramática
        self.input_label = ttk.Label(self.root, text="Ingrese la gramática (ej: S -> Sa|b):")
        self.input_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.grammar_input = tk.Text(self.root, width=50, height=10)
        self.grammar_input.grid(column=0, row=1, padx=10, pady=10)

        # Botón para procesar
        self.process_button = ttk.Button(self.root, text="Eliminar Recursión", command=self.process_grammar)
        self.process_button.grid(column=0, row=2, padx=10, pady=10)

        # Salida de gramática
        self.output_label = ttk.Label(self.root, text="Gramática sin recursión:")
        self.output_label.grid(column=0, row=3, padx=10, pady=10)

        self.grammar_output = tk.Text(self.root, width=50, height=10, state='disabled')
        self.grammar_output.grid(column=0, row=4, padx=10, pady=10)

    def process_grammar(self):
        input_text = self.grammar_input.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showerror("Error", "Por favor, ingrese una gramática.")
            return
        
        try:
            gramatica = self.parse_grammar(input_text)
            nueva_gramatica = eliminar_recursion_directa(gramatica)
            self.display_grammar(nueva_gramatica)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def parse_grammar(self, input_text):
        gramatica = {}
        for line in input_text.splitlines():
            no_terminal, producciones = line.split("->")
            no_terminal = no_terminal.strip()
            producciones = [p.strip() for p in producciones.split('|')]
            gramatica[no_terminal] = producciones
        return gramatica

    def display_grammar(self, gramatica):
        self.grammar_output.config(state='normal')
        self.grammar_output.delete("1.0", tk.END)
        for no_terminal, producciones in gramatica.items():
            self.grammar_output.insert(tk.END, f"{no_terminal} -> {' | '.join(producciones)}\n")
        self.grammar_output.config(state='disabled')
