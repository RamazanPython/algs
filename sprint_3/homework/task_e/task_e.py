def solution(house_amount: int, money: int, prices: list[int]) -> int:
    prices.sort()

    amount = 0
    for price in prices:
        if money >= price:
            money -= price
            amount += 1

        if amount == house_amount:
            break

    return amount


def main():
    n, k = list(map(int, input().strip().split()))
    prices = list(map(int, input().strip().split()))
    print(solution(house_amount=n, money=k, prices=prices))


if __name__ == "__main__":
    main()
