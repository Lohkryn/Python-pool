class Plant:
    name: str
    height: float
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def created(self) -> None:
        print("Created: ", end="")
        self.show()

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    rose.created()
    oak.created()
    cactus.created()
    sunflower.created()
    fern.created()


if __name__ == "__main__":
    ft_plant_factory()
