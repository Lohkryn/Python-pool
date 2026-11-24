def ft_recursive(n, nbr):
    if n <= nbr:
        print(f"Day {n}")
        ft_recursive(n + 1, nbr)


def ft_count_harvest_recursive():
    nbr = int(input("Days until harvest: "))
    ft_recursive(1, nbr)
    print("Harvest time!")
