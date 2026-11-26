class Plant:
    name: str
    height: float
    days: int
    growing: float
    day: int

    def age(self) -> None:
        self.day += 1
        self.days += 1

    def grow(self) -> None:
        self.height += self.growing

    def show(self) -> None:
        if self.day > 0:
            print(f"=== Day {self.day} ===")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")


def ft_plant_growth() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    rose.growing = 0.8
    rose.day = 0
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(0, 7):
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.growing * rose.day, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
