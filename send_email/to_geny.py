import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_to_geny(lab, name, classroom, location):
    # Email Configuration
    sender_email = "your_email@example.com"
    receiver_email = ""
    subject = "Réservation de salle garage isep"
    message = f"""
    Bonjour Madame,

    Le '{lab}' lab organise un workshop titré '{name}'. Nous souhaiterions réserver la salle '{classroom}' dans le campus '{location}'.

    Cordialement,
    Garage Companion
    """
    print(message)

    # Create email message
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject
    email_message.attach(MIMEText(message, "plain"))

    # Send email
    #with smtplib.SMTP("smtp.example.com", 587) as server:
    #    server.login(sender_email, "your_password")
     #   server.send_message(email_message)
    print("Email sent successfully!")
