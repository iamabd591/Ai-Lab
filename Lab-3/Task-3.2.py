def classify_animal():
    print("Animal Classification Decision Tree:")
    print("1. Does the animal have wings?")
    wings = input("Enter 'yes' or 'no': ").lower()

    if wings == 'yes':
        print("2. Can the animal fly?")
        can_fly = input("Enter 'yes' or 'no': ").lower()
        if can_fly == 'yes':
            print("It's a bird.")
        else:
            print("It's a bat.")
    else:
        print("3. Is the animal aquatic?")
        aquatic = input("Enter 'yes' or 'no': ").lower()
        if aquatic == 'yes':
            print("4. Does the animal have gills?")
            has_gills = input("Enter 'yes' or 'no': ").lower()
            if has_gills == 'yes':
                print("It's a fish.")
            else:
                print("It's a mammal, like a dolphin or whale.")
        else:
            print("5. Does the animal have four legs?")
            four_legs = input("Enter 'yes' or 'no': ").lower()
            if four_legs == 'yes':
                print("6. Is the animal kept as a pet?")
                pet = input("Enter 'yes' or 'no': ").lower()
                if pet == 'yes':
                    print("It could be a dog or a cat.")
                else:
                    print("It's a wild mammal, like a lion or tiger.")
            else:
                print("It's a snake.")
def classify_car():
    print("Car Classification Decision Tree:")
    print("1. Is the car electric?")
    electric = input("Enter 'yes' or 'no': ").lower()

    if electric == 'yes':
        print("2. What is the car's range per charge?")
        range_per_charge = float(input("Enter the range in miles: "))
        if range_per_charge >= 300:
            print("It's a high-range electric car.")
        elif 200 <= range_per_charge < 300:
            print("It's a mid-range electric car.")
        else:
            print("It's a low-range electric car.")
    else:
        print("3. What is the car's fuel efficiency in miles per gallon (MPG)?")
        mpg = float(input("Enter the MPG: "))
        if mpg >= 30:
            print("It's a fuel-efficient car.")
        elif 20 <= mpg < 30:
            print("It's a moderately fuel-efficient car.")
        else:
            print("It's a gas-guzzler.")


print("Press 1 For Car CLassify");
print("Press 2 For Animal CLassify");
option = input();
if(option=='1'):
    classify_car()
elif(option=='2'):
    classify_animal()
else:
    print("Wronge Input")
