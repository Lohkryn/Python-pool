def ft_water_reminder():
    time = input("Days since last watering: ")
    if time > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
