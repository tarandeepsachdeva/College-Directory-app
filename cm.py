import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

def show_message():
    messagebox.showinfo("PCTE Navigation", "Welcome to PCTE Campus Navigation System!")

def find_path():
    G = nx.Graph()
    G.add_node("Engineering Block")
    G.add_node("Cafeteria")
    G.add_node("Library")
    G.add_node("Administration Block")
    G.add_node("Computer Science Block")
    G.add_node("Mechanical Block")

    G.add_edge("Engineering Block", "Cafeteria", weight=2)
    G.add_edge("Engineering Block", "Library", weight=3)
    G.add_edge("Cafeteria", "Library", weight=1)
    G.add_edge("Library", "Administration Block", weight=2)
    G.add_edge("Administration Block", "Computer Science Block", weight=3)
    G.add_edge("Computer Science Block", "Mechanical Block", weight=2)
    G.add_edge("Mechanical Block", "Engineering Block", weight=4)

    start_block = "Engineering Block"
    end_block = "Cafeteria"
    shortest_path = nx.dijkstra_path(G, source=start_block, target=end_block)
    messagebox.showinfo("Shortest Path", f"Shortest path from {start_block} to {end_block}: {shortest_path}")

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_color="black")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

root = tk.Tk()
root.title("PCTE Campus Navigation System")

welcome_label = tk.Label(root, text="Welcome to PCTE Campus Navigation System", font=("Helvetica", 16))
welcome_label.pack(pady=20)

start_button = tk.Button(root, text="Start Navigation", command=find_path)
start_button.pack(pady=10)
root.mainloop()