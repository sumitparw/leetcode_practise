def carParkingRoof(cars, k):
    cars = sorted(cars)
    print(cars)
    roof = cars[k - 1] - cars[0] + 1
    print(roof)
    i = 1
    while i + k - 1 < (len(cars)):
        roof_new = cars[i + k - 1] - cars[i] + 1
        if (roof > roof_new):
            roof = roof_new
        i = i + 1
    return (roof)
if __name__ =="__main__":
    k = 3
    cars = [2, 8, 10, 17]
    print(carParkingRoof(cars,k))