def ft_recursive(n: int, nbr: int) -> None:
    if n <= nbr:
        print(f"Day {n}")
        ft_recursive(n + 1, nbr)


def ft_count_harvest_recursive() -> None:
    nbr = int(input("Days until harvest: "))
    ft_recursive(1, nbr)
    print("Harvest time!")
