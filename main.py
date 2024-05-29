import tkinter as tk
from controller.grammar_controller import GrammarController

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarController(root)
    root.mainloop()
