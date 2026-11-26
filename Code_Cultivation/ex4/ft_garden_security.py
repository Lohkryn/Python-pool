class Plant:
    _name: str
    _height: float
    _age: int

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name} Error, height can’t be negative\nHeight update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name} Error, age can’t be negative\nAge update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} age")

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def created(self) -> None:
        print("Plant created: ", end="")
        self.show()

    def current(self) -> None:
        print("Current state: ", end="")
        self.show()

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self.created()
        print("")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    rose.set_age(-5)
    print("")
    rose.current()


if __name__ == "__main__":
    ft_garden_security()
