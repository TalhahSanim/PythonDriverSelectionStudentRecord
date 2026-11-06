'''
Class Driver

Create Constructors
	licence
	Firstname
	LastName
	demerit points

Create functions
	check demerit points of drivers
	add demerit points to specific drivers
	remove demerit points
	display specific driver details
'''


class Driver:
    def __init__(self, licence, first_name, last_name, demerit_points):
        self.licence = licence
        self.first_name = first_name
        self.last_name = last_name
        self.demerit_points = demerit_points

        # Checking the demerit points of the drivers
        # display a warning if points are greater than or equal to 12

    def checkdemerit(self):
        print(f"Checking Demerit Points...\n{self.first_name} has {self.demerit_points} Demerit Points")
        if self.demerit_points >= 12:
            #    WARNING:your demerit points are between 9 to 12 and if they are too low your licence will be suspended"
            print(
                "WARNING:your demerit points are between 9 to 12 and if they are too high your licence will be suspended")
        elif self.demerit_points >= 9:
            print("")

            # add demerit points to driver

    def add_demerit(self):
        print(
            f"Adding Demerit point... value of \n{self.demerit_points + 1} to driver {self.first_name} {self.last_name} ")
        print()
        # delete demerit from driver

    def delete_demerit(self):
        print(
            f"\n{self.demerit_points - 1} {self.first_name} {self.last_name}")
        # display driver details

    def display(self):
        print()
        print("Driver Details")
        print()
        print(f"Licence Number: {self.licence}")
        print(f"First Name:{self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Current Demerit Points: {self.demerit_points}")


'''
create a class called Vehicle
Class Vehicle

 
Make constructors
	 
	Manufacturer
	Registration number
	Specific Model
	Kilometres
	Specific Drivers

create functions
	updating Kilometres
	display information for vehicles

'''


class Vehicle:
    def __init__(self, registration, make, kilometres, driver):
        self.registration = registration
        self.make = make
        self.kilometres = kilometres
        self.driver = driver

    # Update Kilometres for vehicles
    def update_kilometres(self):
        print("Updating Kilometres...")
        default_kilometres = 12345
        self.kilometres = default_kilometres

        # Display Vehicle Details

    def display(self):
        # print("Vehicle Details")
        print(f"Registration: {self.registration}")
        print(f"Make: {self.make}")
        print(f"Kilometres: {self.kilometres}")
        # print(f"Driver: {self.driver}")
        print(f"Driver: {self.driver.first_name} {self.driver.last_name}")


'''
create a class called Truck
Class Truck

Create Constructors
	Max load
	axles
	wheels

create functions
	showing specific information about trucks

'''


class Truck(Vehicle):
    def __init__(self, registration, make, kilometres, driver, max_load, axles, wheels):
        super().__init__(registration, make, kilometres, driver)
        self.max_load = max_load
        self.axles = axles
        self.wheels = wheels

        # Display Truck Details

    def display(self):
        # Display Details for Truck
        print("Trucks Details:")
        print(f"Max Load: {self.max_load}")
        print(f"Axles: {self.axles}")
        print(f"Wheels: {self.wheels}")

        print()

        print(f"Registration: {self.registration}")
        print(f"Make: {self.make}")
        print(f"Kilometres: {self.kilometres}")
        print(f"Driver: {self.driver.first_name} {self.driver.last_name}")


'''
Create class called Car
Class Car

Make constructors

	BodyType
	color
	Upholstery
	Doors

Create functions
	Changing color for cars
	Displaying car information 
'''


class Car(Vehicle):
    def __init__(self, registration, make, kilometres, driver, bodytype, colour, upholstry, doors):
        super().__init__(registration, make, kilometres, driver)
        self.bodytype = bodytype
        self.colour = colour
        self.upholstry = upholstry
        self.doors = doors

        # Display color of the car

    def change_colour(self):
        default_colour = "blue"
        print(f"Colour of car to {default_colour}  ")
        self.colour = default_colour

        # display Car Details

    def display(self):
        print("Car Details")
        print(f"Body Type: {self.bodytype}")
        print(f"Colour: {self.colour}")
        print(f"Upholstry: {self.upholstry}")
        print(f"Number of Doors: {self.doors}")

        print()

        print(f"Registration: {self.registration}")
        print(f"Make: {self.make}")
        print(f"Kilometres: {self.kilometres}")
        print(f"Driver: {self.driver.first_name} {self.driver.last_name}")


def main():
    driver1 = Driver(100, "Jack", "Sun", 5)

    driver2 = Driver(200, "Bob", "Blue", 9)

    car1 = Car(1, "Camry", 1000, driver1, "Sedan", "White", "Fabric", 4)

    truck1 = Truck(3, "Isuzu", 5000, driver2, 30000, 2, 4)

    driver1.checkdemerit()

    driver2.checkdemerit()

    driver1.add_demerit()

    driver2.add_demerit()

    driver1.delete_demerit()

    driver2.delete_demerit()

    driver1.display()

    driver2.display()

    car1.update_kilometres()
    truck1.update_kilometres()

    print()
    print()
    print()

    car1.display()
    car1.change_colour()
    print()
    truck1.display()

    # Source of code is from password manager assessment Programming introductory
    # Writing to a text file 
    print()
    file = open("driver_output.txt", "w")
    file.write(f"\n Driver Documentation")
    file.write(f" \n Driver1 Information\n Licence Number:{driver1.licence}\n First Name:{driver1.first_name}\n Last Name:{driver1.last_name}\n Demerit Points:{driver1.demerit_points}")

    file.write(f" \n Driver2 Information\n Licence Number:{driver2.licence}\n First Name:{driver2.first_name}\n Last Name:{driver2.last_name}\n Demerit Points:{driver2.demerit_points}")

    file.close
    # Source for reading text file: https://www.w3schools.com/python/python_file_open.asp
    #https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python
    file = open("driver_output.txt", "r")
    with open("driver_output.txt","r",encoding="utf-8") as file:
        for line in file:
         print(line.strip())

    file.close


main()
