import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox

class GrammarView:
    def __init__(self, root, process_callback, process_cadena):
        self.root = root
        self.root.title("Crear Tabla LL(k)")
        # Ajustar el tamaño de la ventana
        self.root.geometry("1800x900")
        root.configure(bg="#E0F2F1")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.create_widgets(process_callback, process_cadena)

    def create_widgets(self, process_callback, process_cadena):
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
        self.grammar_frame.grid(column=0, row=0, sticky=tk.N)

        self.input_label = ttk.Label(self.grammar_frame, text="Ingrese la gramática (ej: S -> S a | b):", style="TLabel")
        self.input_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        
        self.grammar_input = tk.Text(self.grammar_frame, width=45, height=10, wrap="word", font=("Cascadia Code", 11))
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

        self.grammar_output = tk.Text(self.grammar_frame, width=45, height=10, wrap="word", font=("Cascadia Code", 11), state='disabled', bg="#E0F2F1")
        self.grammar_output.grid(column=0, row=4, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Marco para los conjuntos primeros y siguientes
        self.functions_table_frame = tk.Frame(main_frame, bg="#E0F2F1")
        self.functions_table_frame.grid(column=1, row=0, sticky=tk.N)

        self.functions_frame = tk.Frame(self.functions_table_frame, bg="#E0F2F1")
        self.functions_frame.grid(column=0, row=0, sticky=tk.N)

        # Salida de los conjuntos Primeros
        self.first_label = ttk.Label(self.functions_frame, text="Conjuntos primeros:", style="TLabel")
        self.first_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        self.first_output = tk.Text(self.functions_frame, width=52, height=10, wrap="word", font=("Cascadia Code", 11), state='disabled', bg="#E0F2F1")
        self.first_output.grid(column=0, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Salida de los conjuntos Siguientes
        self.follow_label = ttk.Label(self.functions_frame, text="Conjuntos siguientes:", style="TLabel")
        self.follow_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)

        self.follow_output = tk.Text(self.functions_frame, width=52, height=10, wrap="word", font=("Cascadia Code", 11), state='disabled', bg="#E0F2F1")
        self.follow_output.grid(column=0, row=3, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Marco para la entrada de cadena
        self.cadena_frame = ttk.Frame(main_frame, padding="10 10 10 10", style="TFrame")
        self.cadena_frame.grid(column=2, row=0, sticky=(tk.N, tk.E), padx=20, pady=10)

        self.cadena_label = ttk.Label(self.cadena_frame, text="Ingrese la cadena (ej: n + n):", style="TLabel")
        self.cadena_label.grid(column=2, row=0, padx=5, pady=5, sticky=tk.W)
        
        self.cadena_input = tk.Entry(self.cadena_frame, width=50, font=("Cascadia Code", 11))
        self.cadena_input.grid(column=2, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.cadena_button = ttk.Button(self.cadena_frame, text="Procesar Cadena", command=process_cadena)
        self.cadena_button.grid(column=2, row=2, padx=5, pady=5, sticky=tk.W)
        
        self.cadena_result = ttk.Label(self.cadena_frame, text="", style="TLabel")
        self.cadena_result.grid(column=2, row=3, padx=5, pady=5, sticky=tk.W)

        # Marco para la imagen del procedimiento
        self.procedure_frame = tk.Frame(self.cadena_frame, bg="#E0F2F1")
        self.procedure_frame.grid(column=2, row=4, pady=20, sticky=(tk.W, tk.E))

        self.procedure_label = tk.Label(self.procedure_frame, text="Procedimiento:", bg="#E0F2F1", fg="#333333", font=("Cascadia Code", 11))
        self.procedure_label.grid(column=2, row=0, pady=9)

        self.procedure_image = tk.Label(self.procedure_frame, bg="#E0F2F1")
        self.procedure_image.grid(column=2, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Marco para la tabla LL
        self.tabla_frame = tk.Frame(main_frame, bg="#E0F2F1")
        self.tabla_frame.grid(column=0, row=2, pady=2, columnspan=3, sticky=(tk.W, tk.E))

        self.tabla_label = tk.Label(self.tabla_frame, text="Tabla LL", bg="#E0F2F1", fg="#333333", font=("Cascadia Code", 11))
        self.tabla_label.grid(column=0, row=0, pady=9)

        self.table_ll = tk.Label(self.tabla_frame, bg="#E0F2F1")
        self.table_ll.grid(column=0, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Configurar pesos de columnas y filas para un redimensionamiento adecuado
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)

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
        self.first_output.config(state='disabled')

    def output_Siguientes(self, Conjuntos):
        self.follow_output.config(state='normal')
        self.follow_output.delete("1.0", tk.END)
        for non_terminal, follow_set in Conjuntos.items():
            self.follow_output.insert(tk.END, f"SIGUIENTE({non_terminal}) = {{{', '.join(follow_set)}}}\n")
        self.follow_output.config(state='disabled')

    def mensaje_error(self, message):
        messagebox.showerror("Error", message)

    def mostrar_tabla(self):
        tabla = PhotoImage(file="./tabla_ll.png")
        self.table_ll.config(image=tabla)
        self.table_ll.image = tabla

    def mostrar_pila(self):
        pila = PhotoImage(file="./parse_table.png")
        self.procedure_image.config(image=pila)
        self.procedure_image.image = pila

    def input_cadena(self):
        return self.cadena_input.get().strip()

    def output_cadena(self, resultado):
        if resultado:
            self.cadena_result.config(text="Aceptado")
        else:
            self.cadena_result.config(text="Rechazado")

if __name__ == "__main__":
    def dummy_callback():
        print("Process callback triggered")
    
    def process_cadena():
        cadena = app.input_cadena()
        print(f"Procesar cadena: {cadena}")
        # Aquí puedes agregar la lógica para procesar la cadena y determinar si es aceptada o rechazada
        # Por ejemplo, podrías llamar a una función de tu parser y pasarle la cadena
        resultado = True  # Cambia esto según el resultado del procesamiento de la cadena
        app.output_cadena(resultado)
        app.mostrar_pila()  # Mostrar la imagen del procedimiento
    
    root = tk.Tk()
    app = GrammarView(root, dummy_callback, process_cadena)
    root.mainloop()
