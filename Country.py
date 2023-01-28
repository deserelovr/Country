#Jasmine Bumbray
#CIS261
#Country

def display_contrylist():
    print("Country List")
    print("COMMAND MENU")
    print("show - Show all country")
    print("add - Add a new country")
    print("remove - Delete country from list")
    print("done - Exit the list")

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.\n")
    else:
        print("There is no country with that code.\n")

def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")

def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code.\n")

def main():
    countries = {"CA": "Canada",
                 "JA": "Japan",
                 "DK": "Denmark"}
    
    display_contrylist()
    while True:        
        command = input("Command: ")
        command = command.lower()
        if command == "show":
            view(countries)   
        elif command == "add":
            add(countries)
        elif command == "remove":
            delete(countries)  
        elif command == "done":
            print("See Ya!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
