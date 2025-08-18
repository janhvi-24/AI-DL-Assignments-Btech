import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the map of Australia (adjacency list)
australia_map = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW', 'T'],
    'T': ['V']
}

# Colors available
colors = ['Red', 'Green', 'Blue']

# Function to check if coloring is valid
def is_valid(region, color, assignment):
    for neighbor in australia_map[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def backtrack(assignment):
    if len(assignment) == len(australia_map):
        return assignment
    
    region = [r for r in australia_map.keys() if r not in assignment][0]
    
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]
    return None

# GUI Application
class MapColoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Coloring Problem (CSP)")
        
        # Button to Solve
        self.solve_button = tk.Button(root, text="Solve Map Coloring", command=self.solve)
        self.solve_button.pack(pady=10)

        # Canvas for drawing graph
        self.frame = tk.Frame(root)
        self.frame.pack()
    
    def solve(self):
        solution = backtrack({})
        self.draw_map(solution)
    
    def draw_map(self, solution):
        G = nx.Graph(australia_map)
        
        pos = nx.spring_layout(G, seed=42)  # layout for positioning
        
        node_colors = [solution.get(node, "white") for node in G.nodes()]
        
        fig, ax = plt.subplots(figsize=(6, 6))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=12, font_weight="bold", edge_color="black")
        
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        plt.close(fig)

# Run the GUI
root = tk.Tk()
app = MapColoringApp(root)
root.mainloop()
