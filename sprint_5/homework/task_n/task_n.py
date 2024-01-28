def sift_up(heap, idx) -> int:
    if heap[idx // 2] > heap[idx] or idx == 1:
        return idx

    heap[idx // 2], heap[idx] = heap[idx], heap[idx // 2]
    return sift_up(heap, idx // 2)


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()
