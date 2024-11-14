import heapq

with open("Input file.txt", "r") as file:
    data = file.readlines()

start_city = input("Start node: ")
end_city = input("Destination: ")

def parse_data(data):
    city_map = {}
    heuristics = {}

    for line in data:
        parts = line.strip().split()
        city = parts[0]
        heuristics[city] = int(parts[1])
        neighbors = {}

        for i in range(2, len(parts), 2):
            neighbor_city = parts[i]
            distance = int(parts[i + 1])
            neighbors[neighbor_city] = distance
        
        city_map[city] = neighbors

    return city_map, heuristics

city_map, heuristics = parse_data(data)

def astar_search(start_city, end_city, city_map, heuristics):
    queue = []
    heapq.heappush(queue, (0, start_city))
    came_from = {}
    path_cost = {}
    came_from[start_city] = None
    path_cost[start_city] = 0

    while queue:
        current_city = heapq.heappop(queue)[1]
        
        if current_city == end_city:
            path = []
            while current_city is not None:
                path.append(current_city)
                current_city = came_from[current_city]
            path.reverse()
            return path, path_cost[end_city]
        
        for neighbor in city_map[current_city]:
            new_cost = path_cost[current_city] + city_map[current_city][neighbor]
            if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                path_cost[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                heapq.heappush(queue, (priority, neighbor))
                came_from[neighbor] = current_city
    
    return None, None

path, total_distance = astar_search(start_city, end_city, city_map, heuristics)

if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total distance: {total_distance} km")
else:
    print("NO PATH FOUND")
