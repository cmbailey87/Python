import smtplib, ssl

port = 465  # For SSL
password1 = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("baileybot87@gmail.com", password1)
    # TODO: Send email here


server = smtplib.SMTP("smtp.gmail.com", port)
server.login("baileybot87@gmail.com", password1)
