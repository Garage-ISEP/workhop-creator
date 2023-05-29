def select_location():
    LOCATIONS = ['NDL', 'NDC', 'Online']

    print("Select the location:")
    for i, location in enumerate(LOCATIONS, 1):
        print(f"{i}. {location}")

    while True:
        choice = input("Enter the location number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(LOCATIONS):
            selected_location = LOCATIONS[int(choice) - 1]
            return selected_location
        else:
            print("Invalid input. Please enter a valid location number.")
