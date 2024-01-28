from collections import deque


def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for v1, v2 in graph:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    for arr in adj_list:
        arr.sort()

    return adj_list


def bfs(start_vertex: int, adj_list: list[list], result: list):
    queue = deque([start_vertex])
    visited = set()
    idx = 0
    while queue:
        u = queue.popleft()
        if u not in visited:
            result[idx] = u
            idx += 1

        visited.add(u)
        for neighbor in adj_list[u]:
            if neighbor not in visited:
                queue.append(neighbor)



def main():
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    start_vertex = int(input().strip())

    adj_list = get_adjacency_list(n, graph)
    result = [0] * n
    bfs(start_vertex, adj_list, result)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
