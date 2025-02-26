import os
import sys
import heapq

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = {i: {} for i in range(num_nodes)}
    
    def add_edge(self, u, v, weight):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u][v] = weight
        else:
            raise KeyError(f"Invalid edge ({u} -> {v}): node index out of range")
    
    def get_edges(self):
        edges = []
        for u in self.adj_list:
            for v in self.adj_list[u]:
                edges.append((u, v, self.adj_list[u][v]))
        return edges


def load_graph(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        num_nodes, num_edges = map(int, lines[0].strip().split())
        graph = Graph(num_nodes)
        for line in lines[1:]:
            u, v, weight = map(int, line.strip().split())
            if u >= num_nodes or v >= num_nodes:
                print(f"Invalid edge ({u} -> {v}) in {filename}: node index out of range")
                exit(1)
            graph.add_edge(u, v, weight)
    return graph


def detect_cycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.adj_list[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    
    for node in graph.adj_list:
        if node not in visited:
            if dfs(node):
                return True
    return False


def has_negative_edge(graph):
    for node in graph.adj_list:
        for neighbor in graph.adj_list[node]:
            if graph.adj_list[node][neighbor] < 0:
                return True
    return False


def dag_shortest_path(graph, source):
    def topological_sort(graph):
        visited = set()
        stack = []
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph.adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)
        
        for node in graph.adj_list:
            if node not in visited:
                dfs(node)
        
        return stack[::-1]
    
    def initialize_single_source(graph, source):
        dist = {node: float('inf') for node in graph.adj_list}
        pred = {node: None for node in graph.adj_list}
        dist[source] = 0
        return dist, pred
    
    def relax(node, neighbor, graph, dist, pred):
        if dist[neighbor] > dist[node] + graph.adj_list[node][neighbor]:
            dist[neighbor] = dist[node] + graph.adj_list[node][neighbor]
            pred[neighbor] = node
    
    topo_order = topological_sort(graph)
    dist, pred = initialize_single_source(graph, source)
    
    for node in topo_order:
        for neighbor in graph.adj_list[node]:
            relax(node, neighbor, graph, dist, pred)
    
    return dist, pred


def dijkstra(graph, source):
    pq = [(0, source)]
    dist = {node: float('inf') for node in graph.adj_list}
    pred = {node: None for node in graph.adj_list}
    dist[source] = 0
    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph.adj_list[node].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                pred[neighbor] = node
                heapq.heappush(pq, (distance, neighbor))
    return dist, pred


def bellman_ford(graph, source):
    dist = {node: float('inf') for node in graph.adj_list}
    pred = {node: None for node in graph.adj_list}
    dist[source] = 0
    edges = graph.get_edges()
    for _ in range(graph.num_nodes - 1):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                pred[v] = u
    for u, v, weight in edges:
        if dist[u] + weight < dist[v]:
            return None, None  # Negative weight cycle detected
    return dist, pred


def compute_shortest_path(graph, source, destination):
    if destination not in graph.adj_list:
        return None, None, None, "Invalid destination node"

    is_dag = not detect_cycle(graph)
    has_negative_edges = has_negative_edge(graph)

    if is_dag:
        print("Your selected graph doesn't have any cycles in it so it is a DAG type graph, so running DAG SP algorithm.")
        algorithm = "DAG SP"
        dist, pred = dag_shortest_path(graph, source)
    else:
        if has_negative_edges:
            print("Your selected graph is non-DAG since it has cycles and has negative edge weights, so running Bellman-Ford algorithm.")
            algorithm = "Bellman-Ford"
            dist, pred = bellman_ford(graph, source)
            if dist is None:
                print("Negative weight cycle detected in the selected graph.")
                sys.exit(1)
        else:
            print("Your selected graph has cycles so it is non-DAG and has no negative edge weights, so running Dijkstra's algorithm.")
            algorithm = "Dijkstra"
            dist, pred = dijkstra(graph, source)
    
    path_length = dist[destination]
    if path_length == float('inf'):
        return algorithm, None, None, "There isn't any path exist between selected node and destination choices, please try another destination."
    else:
        path = []
        current = destination
        while current is not None:
            path.insert(0, current)
            current = pred[current]
        return algorithm, path_length, path, "Success"


def main():
    file_list = [
        "n200_d4_TypeA.edgelist",
        "n200_d14_TypeA.edgelist",
        "n200_d100_TypeA.edgelist",
        "n800_d4_TypeA.edgelist",
        "n800_d28_TypeA.edgelist",
        "n800_d400_TypeA.edgelist",
        "n1400_d4_TypeA.edgelist",
        "n1400_d37_TypeA.edgelist",
        "n1400_d700_TypeA.edgelist",
        "n200_d4_TypeB.edgelist",
        "n200_d14_TypeB.edgelist",
        "n200_d100_TypeB.edgelist",
        "n800_d4_TypeB.edgelist",
        "n800_d28_TypeB.edgelist",
        "n800_d400_TypeB.edgelist",
        "n1400_d4_TypeB.edgelist",
        "n1400_d37_TypeB.edgelist",
        "n1400_d700_TypeB.edgelist",
        "n200_d4_TypeC.edgelist",
        "n200_d14_TypeC.edgelist",
        "n200_d100_TypeC.edgelist",
        "n800_d4_TypeC.edgelist",
        "n800_d28_TypeC.edgelist",
        "n800_d400_TypeC.edgelist",
        "n1400_d4_TypeC.edgelist",
        "n1400_d37_TypeC.edgelist",
        "n1400_d700_TypeC.edgelist",
    ]

    # Display the list of files to the user
    print("Select a graph file from the following list:")
    for idx, file_name in enumerate(file_list, 1):
        print(f"{idx}. {file_name}")

    # Prompt user to select a file
    while True:
        try:
            file_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= file_choice <= len(file_list):
                input_file = file_list[file_choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(file_list))
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Extract the number of nodes from the file name
    num_nodes = int(input_file.split('_')[0][1:])
    print(f"The nodes in the selected graph are in the range 0 to {num_nodes - 1}")

    # Prompt for source node with validation
    while True:
        try:
            source_node = int(input(f"Enter the source node (between 0 and {num_nodes - 1}): "))
            if 0 <= source_node < num_nodes:
                break
            else:
                print(f"Invalid source node. Please enter a number between 0 and {num_nodes - 1}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    graph = load_graph(input_file)

    while True:
        destination_node = input("Enter the destination node (or type 'getaway' to exit): ")
        if destination_node.lower() == 'getaway':
            break
        try:
            destination_node = int(destination_node)
            if 0 <= destination_node < num_nodes:
                algorithm, path_length, path, status = compute_shortest_path(graph, source_node, destination_node)
                if status == "Success":
                    print(f"The shortest path from node {source_node} to node {destination_node} using the {algorithm} algorithm has a path length of {path_length}")
                    print(f"The path is: {' -> '.join(map(str, path))}")
                else:
                    print(f"Failed to find a shortest path because - {status}")
            else:
                print(f"Invalid destination node. Please enter a number between 0 and {num_nodes - 1}")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
