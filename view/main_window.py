import tkinter as tk
from tkinter import ttk, messagebox

class GrammarView:
    def __init__(self, root, process_callback):
        self.root = root
        self.root.title("Eliminación de Recursión en GLC")

        self.create_widgets(process_callback)

    def create_widgets(self, process_callback):
        # Entrada de gramática
        self.input_label = ttk.Label(self.root, text="Ingrese la gramática (ej: S -> Sa|b):")
        self.input_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.grammar_input = tk.Text(self.root, width=50, height=10)
        self.grammar_input.grid(column=0, row=1, padx=10, pady=10)

        # Botón para procesar
        self.process_button = ttk.Button(self.root, text="Eliminar Recursión y Abiguedad", command=process_callback)
        self.process_button.grid(column=0, row=2, padx=10, pady=10)

        # Salida de gramática
        self.output_label = ttk.Label(self.root, text="Gramática sin recursión:")
        self.output_label.grid(column=0, row=3, padx=10, pady=10)

        self.grammar_output = tk.Text(self.root, width=50, height=10, state='disabled')
        self.grammar_output.grid(column=0, row=4, padx=10, pady=10)

    def input_gramatica(self):
        return self.grammar_input.get("1.0", tk.END).strip()

    def output_gramatica(self, gramatica):
        self.grammar_output.config(state='normal')
        self.grammar_output.delete("1.0", tk.END)
        for no_terminal, producciones in gramatica.items():
            self.grammar_output.insert(tk.END, f"{no_terminal} -> {' | '.join(producciones)}\n")
        self.grammar_output.config(state='disabled')

    def mensaje_error(self, message):
        messagebox.showerror("Error", message)
