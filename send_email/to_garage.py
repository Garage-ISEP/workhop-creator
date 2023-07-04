from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from generation.generate_event_description import generate_text


def send_email_to_garage(description):
    subject = generate_text(description)
    # Email Configuration
    sender_email = "your_email@example.com"
    receiver_email = ""
    message = "Email Message"
    print(subject)

    # Create email message
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject
    email_message.attach(MIMEText(message, "plain"))

    # Send email
    #with smtplib.SMTP("smtp.example.com", 587) as server:
     #   server.login(sender_email, "your_password")
    #    server.send_message(email_message)
    print("Email sent successfully!")
