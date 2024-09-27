# import smtplib
#
# my_email = "johnnymont2255@gmail.com"
# password = "ayrghhhjgmcenzfh"
#
# connection = smtplib.SMTP("smtp.gmail.com", 465)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="lemonpart@yahoo.com", msg="Hello")
# connection.close()
import smtplib

# Your email and app-specific password (if 2FA is enabled)
my_email = "johnnymont2255@gmail.com"
password = "ayrghhhjgmcenzfh"  # Use the App Password generated from your Google account

# Connect to Gmail's SMTP server using SSL on port 465
connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# Log in to your Gmail account
connection.login(user=my_email, password=password)

# Send an email
connection.sendmail(
    from_addr=my_email,
    to_addrs="lemonpart@yahoo.com",  # Recipient's email address
    msg="Subject:Test\n\nHello, this is a test email."  # Ensure correct email format with subject and body
)

# Close the connection
connection.close()
