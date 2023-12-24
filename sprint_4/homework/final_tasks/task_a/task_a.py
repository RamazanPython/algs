# ID: 102926745
# Time: O(N^2)
# Space: O(N)
"""
Принцип работы:

Основные идеи были взяты из теории и из доп материалов:
1. https://reintech.io/blog/create-simple-search-engine-with-python
2. https://habr.com/ru/articles/263823/

Первое, что я делаю перед поиском, - создаю поисковой индекс (перевёрнутого индекса). Основная идея заключается
в создании такой структуры:
    {word: {document_number: weight}}

Для начала в методе create_index создается простой индекс с номером документа и указанием, сколько раз
какое слово повторялось. Далее идет преобразования данного индекса в перевернутый индекс.

Далее для каждого запроса мы ищем число вхождений в каждом документе и ставим веса. Перед этим я преобразую все слова
в запросе в множество (для удаления дубликатов). Веса я храню в массиве, где элементы являются массивом вида:
    [doc_number, weight]

Это сделано, чтобы было можно отсортировать массив по ключу с помощью лямбды (ключ указываем второй элемент массива)

Далее после сортировки выводим результаты в STDOUT

Временная сложность алгоритмы N^2, так как я использую вложенный цикл для создагия перервернутого индекса и при постановке
весов.

Пространственная сложность O(N), где N - количество слов

UPD: Сдаюсь. Не знаю как это сделать за O(N). Попробовал через heapq, но он медленнее чем обычный метод сортировки.
Похоже обычные методы в лоб у меня получаются лучше, чем замудренные решение
"""
from collections import Counter


def create_index(documents: list[str]) -> dict:
    # Convert to {doc_num: occurrence}
    indices = {}
    for doc_num, document in enumerate(documents, start=1):
        words = document.strip().split()
        indices[doc_num] = Counter(words)

    # Convert to {word: {doc_num: occurrence}}
    result = {}
    for doc_num, words in indices.items():
        for word, occurrence in words.items():
            if word not in result:
                result[word] = {}

            if doc_num not in result[word]:
                result[word][doc_num] = occurrence

    return result


def find_documents(indices: dict, request: str, doc_amount: int) -> list:
    words = set(request.strip().split())
    weights = [[i, 0] for i in range(doc_amount + 1)]
    for word in words:
        if word not in indices:
            continue

        documents = indices.get(word, {})
        for document_num, occurrence in documents.items():
            weights[document_num][-1] += occurrence

    return weights


def main() -> None:
    document_amount = int(input().strip())
    documents = []
    for _ in range(document_amount):
        document = input().strip()
        documents.append(document)

    limit = 5
    search_index = create_index(documents)
    request_amount = int(input().strip())
    for _ in range(request_amount):
        request = input().strip()
        weights_by_requests = find_documents(search_index, request, doc_amount=len(documents))
        sorted_documents = sorted(weights_by_requests, key=lambda x: x[1], reverse=True)
        print(" ".join(str(doc_num) for doc_num, amount in sorted_documents[:limit] if doc_num != 0 and amount != 0))


if __name__ == "__main__":
    main()
