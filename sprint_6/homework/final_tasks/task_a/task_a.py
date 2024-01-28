import heapq


def get_max_spanning_tree_weight(adj_list: list) -> int | str:
    start_vertex = 1

    max_heap = []
    for vertex, weight in adj_list[start_vertex]:
        # Transform minheap to maxheap by this multiplication
        # https://stackoverflow.com/a/44352853
        heapq.heappush(max_heap, [-weight, start_vertex, vertex])

    visited = set()
    visited.add(start_vertex)
    max_weight = 0
    while len(visited) < len(adj_list) - 1 and max_heap:
        weight, n1, n2 = heapq.heappop(max_heap)
        if n2 in visited:
            continue

        max_weight += -weight
        visited.add(n2)
        for neighbor, weight in adj_list[n2]:
            if neighbor not in visited:
                heapq.heappush(max_heap, [-weight, n2, neighbor])

    if len(visited) != len(adj_list) - 1:
        return "Oops! I did it again"

    return max_weight


def main():
    n, m = list(map(int, input().strip().split()))
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2, weight = list(map(int, input().strip().split()))
        adj_list[v1].append((v2, weight))
        adj_list[v2].append((v1, weight))

    max_weight = get_max_spanning_tree_weight(adj_list)
    print(max_weight)


if __name__ == "__main__":
    main()
