def sift_down(heap, idx) -> int:
    while idx * 2 < len(heap):
        next_idx = idx * 2
        if next_idx + 1 < len(heap) and heap[next_idx + 1] > heap[next_idx]:
            next_idx += 1

        if heap[idx] > heap[next_idx]:
            break

        heap[idx], heap[next_idx] = heap[next_idx], heap[idx]
        idx = next_idx

    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
