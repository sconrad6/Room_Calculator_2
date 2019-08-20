# take in the user's data
cont = "y"
while cont == "y":

    length = int(input("Enter the length of the room:"))
    width = int(input("Enter the width of the room:"))


    def calculate_area():
        return length * width


    def calculate_perimeter():
        return (length * 2) + (width * 2)

    def calculate_volume():
        return length * height * width


    print(calculate_area())
    print(calculate_perimeter())

    perimeter_choice = input("Would you like to calculate the volume? Y/N").lower()
    if perimeter_choice == "y":
        height = int(input("Please enter the room's height:"))
        print(calculate_volume())

    cont = input("Would you like to continue? Y/N").lower()


print("Goodbye")
