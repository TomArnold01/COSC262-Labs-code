"""Demo of the generic python code runner pseudo-question"""
import matplotlib.pyplot as plt
from graphviz import Graph

# First some simple text output.
vertices = [(0, 0), (100, 0), (1, 50), (100, 100), (0, 100), (0,0)]
vx, vy = zip(*vertices)  # Unpack them
points = [(1, 1), (20, 20), (20, 80), (60, 50),
     (97, 1), (1, 48), (1, 52), (97, 99), (1, 99)]
px, py = zip(*points) # Unpack
print("Vertex x values:", vx)
print("Vertex y values:", vy)
print("Point x values:", px)
print("Point y values:", py)

# Now a matplotlib graph.
axes = plt.axes()
axes.plot(vx, vy, color='blue', marker='o', linestyle='--')
axes.plot(px, py, color='red', marker='x', linestyle='')
axes.set_title('The example from the geometry lecture notes')

# Lastly a graphviz example
g = Graph()
g.node('Root', '23')
g.node('Leaf1', '13', shape='box')
g.node('Leaf2', '99', shape='box')
g.edge('Root', 'Leaf1')
g.edge('Root', 'Leaf2')
g.render('graph', format='png', view=True)