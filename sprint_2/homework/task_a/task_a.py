def solution(rows: int, columns: int, matrix: list[list[int]]) -> list[list[int]]:
    result_matrix = []
    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        result_matrix.append(row)

    return result_matrix


def main() -> tuple:
    rows = int(input().strip())
    columns = int(input().strip())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    return rows, columns, matrix


if __name__ == "__main__":
    rows, columns, matrix = main()
    result_matrix = solution(rows, columns, matrix)
    for elem in result_matrix:
        print(" ".join(map(str, elem)))
