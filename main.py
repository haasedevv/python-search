from queue import PriorityQueue
import heapq
import math

# graph of cities and distances between them
graph = {
    'Vitoria': {'Vila Velha': 10, 'Cariacica': 8, 'Serra': 21},
    'Vila Velha': {'Vitoria': 10, 'Cariacica': 15, 'Viana': 11, 'Guarapari': 40},
    'Cariacica': {'Vitoria': 8, 'Viana': 15, 'Vila Velha': 14},
    'Serra': {'Vitoria': 20, 'Fundao': 25, 'Cariacica': 19},
    'Viana': {'Cariacica': 15, 'Guarapari': 30, 'Vila Velha': 12},
    'Fundao': {'Serra': 25, 'Santa Teresa': 40},
    'Guarapari': {'Viana': 30, 'Anchieta': 45, 'Vila Velha': 40},
    'Santa Teresa': {'Fundao': 40, 'Itarana': 35, 'Santa Maria de Jetiba': 19},
    'Anchieta': {'Guarapari': 45, 'Piúma': 50},
    'Itarana': {'Santa Teresa': 35, 'Santa Maria de Jetiba': 23},
    'Piúma': {'Anchieta': 50, 'Itapemirim': 45},
    'Santa Maria de Jetiba': {'Itarana': 23},
    'Marataizes': {'Piúma': 25, 'Itapemirim': 70},
    'Mucurici': {'Ponto Belo': 5, 'Montanha': 40},
    'Itapemirim': {'Marataizes': 70, 'Piúma': 44}
}

# approximate geographic coordinates of the cities
coordinates = {
    'Vitoria': (40, 20),
    'Vila Velha': (35, 20),
    'Cariacica': (35, 25),
    'Serra': (40, 30),
    'Viana': (30, 25),
    'Fundao': (40, 35),
    'Guarapari': (25, 15),
    'Santa Teresa': (45, 35),
    'Anchieta': (20, 10),
    'Itarana': (45, 30),
    'Piúma': (15, 5),
    'Santa Maria de Jetiba': (50, 35),
    'Marataizes': (10, 5),
    'Mucurici': (60, 10),
    'Itapemirim': (10, 0)
}


 # Defines the heuristic function (estimate of distance to the goal)
def heuristic(node, goal):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Defines the A* search function
def a_star(graph, start, end):
    heap = [(0, start)]
    visited = set()
    path = {}
    cost = {}
    path[start] = []
    cost[start] = 0
    
    while heap:
        (current_cost, current_node) = heapq.heappop(heap)
        
        if current_node == end:
            path_str = ' -> '.join(path[current_node] + [end])
            return (path_str, cost[current_node])
        
        if current_node not in visited:
            visited.add(current_node)
            
            for neighbor, distance in graph[current_node].items():
                updated_neighbor_cost = current_cost + distance + heuristic(neighbor, end)
                
                if neighbor not in cost or updated_neighbor_cost < cost[neighbor]:
                    cost[neighbor] = updated_neighbor_cost
                    path[neighbor] = path[current_node] + [current_node]
                    heapq.heappush(heap, (updated_neighbor_cost, neighbor))
    
    return None

def greedy_search(graph, start, end):
    visited = []
    heap = [(0, start)]
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == end:
            visited.append(current)
            break
        if current not in visited:
            visited.append(current)
            neighbor_costs = []
            for neighbor in graph[current]:
                if neighbor not in visited:
                    neighbor_costs.append((graph[current][neighbor], neighbor))
            if neighbor_costs:
                lowest_cost, lowest_cost_neighbor = min(neighbor_costs)
                heapq.heappush(heap, (cost + lowest_cost, lowest_cost_neighbor))
    return visited, cost

def main():
    try:
        while True:  
            print('|===================|    Rota    |====================|\n| |\n| Digite 1 para comecar usando busca heuristica       |\n| Digite 2 para comecar usando busca gulosa            |\n| Ou 3 para sair do Rota                              |\n|=====================================================|')
            
           
        
            if option == 3:
                print('\n')
                print('Até a próxima ;)')
                print('\n\n')
                break
            else:
                if option == 1:
                    print('\n')
                    start_city = str(input('INSIRA A SUA CIDADE DE ORIGEM: '))
                    destination_city = str(input('INSIRA A CIDADE DE DESTINO: '))
                    print('\n')
                    result = a_star(graph, start_city, destination_city)
                    if result:
                        print('Usando Busca Heuristica!')
                        print(f'Caminho percorrido: {result[0]}')
                        print(f'Custo total: {result[1]}')
                    else:
                        print(f'Não foi possível encontrar um caminho entre {start_city} e {destination_city}.')
                    print('\n\n')
                elif option == 2:
                    print('\n')
                    start = str(input('INSIRA A SUA CIDADE DE ORIGEM: '))
                    end = str(input('INSIRA A CIDADE DE DESTINO: '))
                    print('\n')
                    visited, cost = greedy_search(graph, start, end)
                    print('Usando Busca Gulosa!')
                    print(f'Caminho percorrido: {" -> ".join(visited)}')
                    print(f'Custo total: {cost}')
                    print('\n\n')
                else:
                    print('\n')
                    print('Cidade de origem ou de destino está inválida e/ou não existe!!!')
                    print('\n\n')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()