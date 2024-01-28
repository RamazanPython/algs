from collections import deque


def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for v1, v2 in graph:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    for arr in adj_list:
        arr.sort()

    return adj_list


def bfs(start_vertex: int, adj_list: list[list]):
    queue = deque([start_vertex])
    distances = [None] * len(adj_list)
    prev = [None] * len(adj_list)
    colors = ["white"] * len(adj_list)

    distances[start_vertex] = 0
    colors[start_vertex] = "grey"
    max_distance = 0
    while queue:
        u = queue.popleft()
        for neighbor in adj_list[u]:
            if colors[neighbor] == "white":
                distances[neighbor] = distances[u] + 1
                max_distance = max(max_distance, distances[neighbor])
                prev[neighbor] = u
                colors[neighbor] = "grey"
                queue.append(neighbor)
        colors[u] = "black"

    return max_distance


def main():
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    start_vertex = int(input().strip())

    adj_list = get_adjacency_list(n, graph)
    max_distance = bfs(start_vertex, adj_list)
    print(max_distance)


if __name__ == "__main__":
    main()
