def remove_duplicates(clubs: list[str]) -> list[str]:
    # To keep order I use dict
    unique = {}
    for club in clubs:
        unique[club] = 1 + unique.get(club, 0)

    return list(unique.keys())


def main() -> None:
    n = int(input().strip())
    clubs = []
    for _ in range(n):
        name = input().strip()
        clubs.append(name)

    unique_clubs = remove_duplicates(clubs)
    for club in unique_clubs:
        print(club)


if __name__ == "__main__":
    main()
