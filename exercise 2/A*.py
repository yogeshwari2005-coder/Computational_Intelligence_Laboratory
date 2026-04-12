class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, n1, n2, cost):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1].append((n2, cost))
            self.adj[n2].append((n1, cost))

    def display(self):
        for i in self.adj:
            print(i, "->", self.adj[i])


def a_star_search(graph, start, goal, heuristic):
    open_list = [start]
    closed_list = []

    g = {start: 0}
    # f[n] = g[n] + h(n)
    f = {start: heuristic[start]}
    parent = {start: None}

    step = 1
    print("\n" + "="*50)
    print(f"{'A* SEARCH PROCESS':^50}")
    print("="*50)

    while open_list:
        current = min(open_list, key=lambda x: f[x])

        print(f"\n[STEP {step}]")
        print(f"Current Node: {current}")
        print(f"Open List (Frontier):  {[(node, f'f={f[node]}') for node in open_list]}")
        print(f"Closed List (Visited): {closed_list}")

        # Check if we reached the goal
        if current == goal:
            print(f"\n>> Goal '{goal}' reached!")
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g[goal]

        open_list.remove(current)
        closed_list.append(current)

        # Explore neighbors
        for neighbor, cost in graph.adj[current]:
            if neighbor in closed_list:
                continue

            tentative_g = g[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g >= g.get(neighbor, float('inf')):
                # not a better path
                continue

            # path is the best so far, record it
            parent[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = g[neighbor] + heuristic[neighbor]

            print(f"  -> Found neighbor '{neighbor}': g={g[neighbor]}, h={heuristic[neighbor]}, f={f[neighbor]}")

        step += 1

    return None, float('inf')


# --- Main Execution ---

graph = Graph()

try:
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        graph.add_node(input("Enter node name: "))

    e = int(input("Enter number of edges: "))
    for _ in range(e):
        n1 = input("Enter node 1: ")
        n2 = input("Enter node 2: ")
        cost = int(input(f"Enter edge cost between {n1} and {n2}: "))
        graph.add_edge(n1, n2, cost)

    heuristic = {}
    print("\n--- Enter Heuristic values ---")
    for node in graph.adj:
        heuristic[node] = int(input(f"Heuristic for {node}: "))

    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")

    path, cost = a_star_search(graph, start, goal, heuristic)

    #print("\n" + "="*50)
    if path:
        print(f"\nFINAL PATH: {' -> '.join(path)}")
        print(f"TOTAL COST: {cost}")
    else:
        print("RESULT: No path found.")
    #print("="*50)

except KeyError as e:
    print(f"Error: Node {e} was not found in the graph definition.")
except ValueError:
    print("Error: Please enter valid numbers for counts and costs.")
