class Plant:
    name: str
    height: int
    days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant()
    sunflower = Plant()
    cactus = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.days = 30
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.days = 45
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.days = 120

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
