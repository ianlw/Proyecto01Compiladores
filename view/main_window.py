import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox

from matplotlib.pyplot import style

class GrammarView:
    def __init__(self, root, process_callback):
        self.root = root
        self.root.title("Eliminación de Recursión y/o Ambigüedad en GLC")
        # self.root.geometry("1040x560")
        root.configure(bg="#E0F2F1")
        # self.table = TableController()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.create_widgets(process_callback)

    def create_widgets(self, process_callback):
        # Configuración del estilo
        self.style.configure("TLabel", font=("Helvetica", 11), padding=5, foreground="#333333", background="#E0F2F1")
        self.style.configure("TButton", font=("Helvetica", 11), padding=5, foreground="#333333", background="#81C784", borderwidth=0)
        self.style.map("TButton", background=[("active", "#4CAF50")])
        self.style.configure("TText", font=("Consolas", 12))
        self.style.configure("TFrame", background="#E0F2F1")

        # Marco principal
        main_frame = ttk.Frame(self.root, padding="10 10 10 10", style="TFrame")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Entrada de gramática
        self.grammar_frame = tk.Frame(main_frame, bg="#E0F2F1")
        self.grammar_frame.grid(column=0, row=0)

        self.input_label = ttk.Label(self.grammar_frame, text="Ingrese la gramática (ej: S -> S a | b):", style="TLabel")
        self.input_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        
        self.grammar_input = tk.Text(self.grammar_frame, width=30, height=7, wrap="word", font=("Cascadia Code", 11))
        self.grammar_input.grid(column=0, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Botón para procesar
        self.process_button = ttk.Button(self.grammar_frame, text="Calcular", command=process_callback)
        self.process_button.grid(column=0, row=2, padx=10, pady=10, sticky='')

        # Agregar columnas vacías a cada lado para centrar el botón
        self.grammar_frame.grid_columnconfigure(0, weight=1)
        self.grammar_frame.grid_columnconfigure(2, weight=1)

        # Salida de gramática
        self.output_label = ttk.Label(self.grammar_frame, text="Gramática sin recursión ni ambigüedad:", style="TLabel")
        self.output_label.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)

        self.grammar_output = tk.Text(self.grammar_frame, width=30, height=7, wrap="word", font=("Cascadia Code", 11), state='disabled', bg="#E0F2F1")
        self.grammar_output.grid(column=0, row=4, padx=5, pady=5, sticky=(tk.W, tk.E))

        self.functions_table_frame = tk.Frame(main_frame, bg="#E0F2F1")
        self.functions_table_frame.grid(column=1, row=0, sticky=tk.N)

        self.functions_frame = tk.Frame(self.functions_table_frame, bg="#E0F2F1")
        self.functions_frame.grid(column=0, row=0, sticky=tk.N)

        # Salida de los conjuntos Primeros
        self.output_label = ttk.Label(self.functions_frame, text="Conjuntos primeros:", style="TLabel")
        self.output_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        self.first_output = tk.Text(self.functions_frame, width=35, height=7, wrap="word", font=("Cascadia Code", 11), state='disabled', bg="#E0F2F1")
        self.first_output.grid(column=0, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Salida de los conjuntos Siguientes
        self.output_label = ttk.Label(self.functions_frame, text="Conjuntos siguientes:", style="TLabel")
        self.output_label.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)

        self.follow_output = tk.Text(self.functions_frame, width=35, height=7, wrap="word", font=("Cascadia Code", 11), state='disabled', bg="#E0F2F1")
        self.follow_output.grid(column=1, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        self.tabla_frame = tk.Frame(self.functions_table_frame, bg="#E0F2F1")
        self.tabla_frame.grid(column=0, row=1, pady=2)

        self.tabla_label = tk.Label(self.tabla_frame, text="Tabla LL", bg="#E0F2F1", fg="#333333", font=("Cascadia Code", 11))
        self.tabla_label.grid(column=0, row=0, pady=9)

        self.table_ll = tk.Label(self.tabla_frame, bg="#E0F2F1")
        self.table_ll.grid(column=0, row=4, padx=5, pady=5, sticky=(tk.W, tk.E))

    def input_gramatica(self):
        return self.grammar_input.get("1.0", tk.END).strip()

    def output_gramatica(self, gramatica):
        self.grammar_output.config(state='normal')
        self.grammar_output.delete("1.0", tk.END)
        for no_terminal, producciones in gramatica.items():
            self.grammar_output.insert(tk.END, f"{no_terminal} -> {' | '.join(producciones)}\n")
        self.grammar_output.config(state='disabled')

    def output_Primeros(self, Conjuntos):
        self.first_output.config(state='normal')
        self.first_output.delete("1.0", tk.END)
        for non_terminal, first_set in Conjuntos.items():
            self.first_output.insert(tk.END, f"PRIMERO({non_terminal}) = {{{', '.join(first_set)}}}\n")
        self.grammar_output.config(state='disabled')

    def output_Siguientes(self, Conjuntos):
        self.follow_output.config(state='normal')
        self.follow_output.delete("1.0", tk.END)
        for non_terminal, follow_set in Conjuntos.items():
            self.follow_output.insert(tk.END, f"SIGUIENTE({non_terminal}) = {{{', '.join(follow_set)}}}\n")
        self.grammar_output.config(state='disabled')

    def mensaje_error(self, message):
        messagebox.showerror("Error", message)
    
    def mostrar_tabla(self):
        tabla = PhotoImage(file="./tabla_ll.png")
        self.table_ll.config(image=tabla)
        self.table_ll.image = tabla

#
# if __name__ == "__main__":
#     def dummy_callback():
#         print("Process callback triggered")
#     
#     root = tk.Tk()
#     app = GrammarView(root, dummy_callback)
#     root.mainloop()
