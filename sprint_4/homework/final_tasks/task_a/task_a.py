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
        weights = find_documents(search_index, request, doc_amount=len(documents))
        sorted_documents = sorted(weights, key=lambda x: x[1], reverse=True)
        print(" ".join(str(doc_num) for doc_num, amount in sorted_documents[:limit] if doc_num != 0 and amount != 0))


if __name__ == "__main__":
    main()
