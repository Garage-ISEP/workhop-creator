def select_lab():
    LABS = ['IA', '️Cyber', 'Coder', 'Meta', 'Blockchain', 'Maker']
    print("Select a lab:")
    for i, lab in enumerate(LABS, 1):
        print(f"{i}. {lab}")

    while True:
        choice = input("Enter the lab number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(LABS):
            selected_lab = LABS[int(choice) - 1]
            return selected_lab
        else:
            print("Invalid input. Please enter a valid lab number.")
