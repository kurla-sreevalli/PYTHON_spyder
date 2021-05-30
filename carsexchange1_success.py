class Automobile:

    def __init__(self):
        self.make = " "
        self.model = " "
        self.color = " "
        self.year = 0
        self.mileage = 0


    def add_vehicle(self):
        self.year = int(input("Enter year: "))
        self.make = input("Enter make: ")
        self.model = input("Enter model: ")
        self.color = input("Enter color: ")
        self.mileage = int(input("Enter mileage: "))

    def __str__(self):
         return('%d %s %s Color: %s Mileage: %d' %
              (self.year, self.make, self.model, self. color,
               self.mileage))
        

vehicle_list = []


def edit(vehicle_list):
    pos = int(input('Enter the position of the vehicle to edit: '))
    new_vehicle = car.add_vehicle()
    new_vehicle = car.__str__()
    vehicle_list[pos-1] = new_vehicle
    print('Vehicle was updated')

user=True
while user:
    print ("""
    1.Add Vehicle to Stock
    2.Delete Vehicle from Stock
    3.View Current Stock
    4.Update Vehicle in Stock
    5.Export Current Stock
    6.Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        car = Automobile()
        car.add_vehicle()
        vehicle_list.append(car.__str__())

    elif ans=="2":
        for i in vehicle_list:
            vehicle_list.pop(int(input('Enter position of vehicle to remove: ')))
            print('Successfully removed vehicle')
    elif ans=="3":
        print(vehicle_list)
    elif ans=="4":
        edit(vehicle_list)
    elif ans=='5':
        f = open('vehicle_inv.txt', 'w')
        f.write(str(vehicle_list))
        f.close()
    elif ans=='6':
        print("Thank You For Visiting")
        break
    else:
        print('try again')
