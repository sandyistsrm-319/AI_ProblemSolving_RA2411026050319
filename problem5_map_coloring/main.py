regions = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

solution = {}

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def solve():
    for region in regions:
        for color in colors:
            if is_valid(region, color):
                solution[region] = color
                break

solve()

print("Map Coloring Solution:")
for region in solution:
    print(region, "->", solution[region])
