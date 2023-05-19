import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    # Create a dictionary to store the shortest distances from start to all other nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a dictionary to store the predecessor of each node in the shortest path from start
    predecessors = {node: None for node in graph}

    # Create a list of unvisited nodes and heapify it
    unvisited_nodes = [(distance, node) for node, distance in distances.items()]
    heapq.heapify(unvisited_nodes)

    # Create a NetworkX graph to visualize the search
    G = nx.Graph()
    G.add_nodes_from(graph.keys())
    G.add_weighted_edges_from([(u, v, w) for u in graph for v, w in graph[u].items()])

    # Set fixed positions for the nodes
    pos = nx.spring_layout(G, seed=42)

    while unvisited_nodes:
        # Get the node with the smallest distance from the heap
        current_distance, current_node = heapq.heappop(unvisited_nodes)

        # If we have found the end node, we can return the shortest path
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = predecessors[current_node]
            path.reverse()
            return path, distances[end], G

        # If we have not yet found the end node, visit all its neighbors
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            # Update the distance to this neighbor if it is shorter than the previous distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node

                # Update the heap with the new distance
                for i, (distance, node) in enumerate(unvisited_nodes):
                    if node == neighbor:
                        unvisited_nodes[i] = (new_distance, neighbor)
                        break
                else:
                    heapq.heappush(unvisited_nodes, (new_distance, neighbor))

        # Update the NetworkX graph with the visited nodes and edges
        visited_nodes = set(predecessors.keys()) - set([None])
        visited_edges = [(predecessors[v], v) for v in visited_nodes]
        G.remove_edges_from(visited_edges)
        nx.set_node_attributes(G, {v: {'color': 'green'} for v in visited_nodes})
        nx.set_node_attributes(G, {current_node: {'color': 'red'}})

        # Draw the NetworkX graph with fixed node positions
        node_colors = nx.get_node_attributes(G, 'color').values()
        nx.draw(G, pos, with_labels=True, node_color=node_colors, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Show the plot and pause for visualization
        plt.show(block=False)
        plt.pause(2)
        plt.clf()

    # If we have visited all nodes and haven't found the end node, there is no path
    return None, None, G
