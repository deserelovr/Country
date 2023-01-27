#Jasmine Bumbray
#CIS261
#Country

def display_contrylist():
    print("Country List")
    print("COMMAND MENU")
    print("list - Show all country")
    print("add - Add a new country")
    print("remove - Delete country from list")
    print("done - Exit the list")

def list(contry_list):
    for c, county in enumerate(contry_list, start=1):
        print(f"{c}, {country}")
    print()

def add(contry_list):
    country = input("Enter Country name: ")
    contry_list.append(country)
    print(f"{country} has been added. \n")

def remove(contry_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contry_list):
        print("Invalid Country number. \n")
    else:
        country = contry_list.pop(number-1)
        print(f"{country} has been delete. /n")
