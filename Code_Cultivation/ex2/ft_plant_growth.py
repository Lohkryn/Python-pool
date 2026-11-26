class Plant:
    name: str
    height: float
    days: int

    def grow(self) -> None:
        
    def show(self) -> None:
        print(f"{self.name}: {round(self.height)}cm, {self.days} days old")



def ft_plant_growth() -> None:
    day = 1
    growth = 0.0
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.days = 30
    rose.show()
    for i in range(1, 7):
        print(f"=== Day {day} ===")
        rose.show()
        rose.height += 0.8
        growth += 0.8
        rose.days += 1
    print(f"Growth this week: {round(growth)}cm")


if __name__ == "__main__":
    ft_plant_growth()
