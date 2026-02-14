import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient_email):
    """Function that takes an email parameter and sends data"""
    
    
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Login Successful"
    
    
    body = "Your login was successful!"
    message.attach(MIMEText(body, "plain"))
    
   
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error: {e}"


if input('Username: ') == 'admin':
    print('Username correct')
    if input('Password: ') == 'secret':
        print('Login successful')
        email = input('Enter your email: ')
        result = send_email(email)
        print(result) 
    else:
        print('Login failed')
else:
    print('Username incorrect')