from unreliable_car import UnreliableCar

my_bad_car = UnreliableCar("Unreliable", 100, 50)

for i in range(1, 11):
    drive_distance = my_bad_car.drive(20)
    print(f"Attempt {i}: Tried to drive 20km, actually drove {drive_distance}km")