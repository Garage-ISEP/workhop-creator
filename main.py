from generate_insta_post import generate_instagram_post
from workshop_information.labs import select_lab
from workshop_information.description import get_description
from workshop_information.datetime_picker import get_date_and_hour
from workshop_information.location import select_location
from workshop_information.classroom import enter_classroom
from workshop_information.name import get_event_name
from send_email.to_garage import send_email_to_garage
from send_email.to_geny import send_email_to_geny


def main():
    while True:
        lab = select_lab()
        event_name = get_event_name()
        description = get_description()
        date, hour = get_date_and_hour()
        location = select_location()
        classroom = enter_classroom()

        # Print the collected information
        print("Workshop Information:")
        print(f"Lab: {lab}")
        print(f"Event Name: {event_name}")
        print(f"Description: {description}")
        print(f"Date: {date}")
        print(f"Hour: {hour}")
        print(f"Location: {location}")
        print(f"Classroom: {classroom}")

        valid = input("Are the above details correct? (yes/no): ")
        if valid.lower() == "yes":
            generate_instagram_post(event_name, lab, description, date, hour, location, classroom)
            while True:
                confirmation = input("Do you want to send the email? (yes/no): ")
                if confirmation.lower() == "yes":
                    # Send email to Geny
                    send_email_to_geny(lab, event_name, classroom, location)
                    # Send email to Garage
                    send_email_to_garage(description)
                    print("Emails sent successfully.")
                    break
                elif confirmation.lower() == "no":
                    print("Emails not sent.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            break
        else:
            print("Let's start again.\n")


if __name__ == "__main__":
    main()
