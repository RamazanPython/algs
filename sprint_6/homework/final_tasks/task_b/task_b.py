def has_cycle(start_vertex: int, adj_list: list, colors: list) -> bool:
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if colors[vertex] == "white":
            colors[vertex] = "grey"
            stack.append(vertex)

            for neighbor in adj_list[vertex]:
                if colors[neighbor] == "white":
                    stack.append(neighbor)
                elif colors[neighbor] == "grey":
                    return True
        elif colors[vertex] == "grey":
            colors[vertex] = "black"

    return False


def is_optimum(adj_list: list) -> bool:
    colors = ["white"] * len(adj_list)
    for i in range(1, len(adj_list)):
        if has_cycle(i, adj_list, colors):
            return False

    return True


def main():
    city_count = int(input().strip())
    adj_list = [[] for _ in range(city_count + 1)]
    for city in range(1, city_count):
        roads = input().strip()
        for idx, road in enumerate(roads, start=1):
            if road == "B":
                adj_list[city].append(city + idx)
            else:
                adj_list[city + idx].append(city)

    if is_optimum(adj_list):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
