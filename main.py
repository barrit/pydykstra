import sys
import modules.dijkstra as dijkstra

def main(args):
    graph1 = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
    }
    graph2 = {
    'A': {'B': 1, 'C': 4, 'D': 10},
    'B': {'C': 1, 'D': 4},
    'C': {'D': 1},
    'D': {}
    }

    path, distance, g = dijkstra.dijkstra(graph2, 'A', 'D')
    print(path)
    print(distance)

if __name__ == '__main__':
    main(sys.argv)