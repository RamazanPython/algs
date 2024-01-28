"""
Задача A.

Алла пошла на стажировку в студию графического дизайна, где ей дали такое задание: для очень большого числа
ориентированных графов преобразовать их список рёбер в список смежности. Чтобы побыстрее решить эту задачу, она
решила автоматизировать процесс.

Помогите Алле написать программу, которая по списку рёбер графа будет строить его список смежности.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100) и число ребер m (1 ≤ m ≤ n(n-1)). В следующих m строках заданы ребра
в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите информацию о рёбрах, исходящих из каждой вершины.

В строке i надо написать число рёбер, исходящих из вершины i, а затем перечислить вершины, в которые ведут эти рёбра
–— в порядке возрастания их номеров.

Принцип работы:

В данной версии решения я использую динамический массив вместо ассоциативного. Получилось не сильно быстрее, чем
с ипользованием словаря.
"""


def get_adjacency_list(vertex_amount: int, graph: list[list[int]]) -> list[list]:
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for edge in graph:
        v1, v2 = edge
        adj_list[v1].append(v2)

    return adj_list


def main() -> None:
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    adj_list = get_adjacency_list(n, graph)
    res = [[] for _ in range(n)]
    for idx, vertices in enumerate(adj_list[1:]):
        res[idx].append(len(vertices))
        for v in vertices:
            res[idx].append(v)

        res[idx] = " ".join(map(str, res[idx]))

    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
