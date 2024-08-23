import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def send_email(subject, body, to_emails):
    # Remove duplicate emails
    to_emails = list(set(to_emails))
    
    # Your Gmail credentials
    from_email = "your_email@gmail.com"  # Replace with your Gmail address
    password = "your_app_specific_password"  # Replace with your app-specific password

    # Setup the Gmail server connection
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(from_email, password)

        for to_email in to_emails:
            # Create the message object
            msg = MIMEMultipart("alternative")
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the HTML body with the msg instance
            msg.attach(MIMEText(body, 'html'))

            # Send the email
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)

            print(f"Email sent successfully to {to_email}!")
            
            # Delay between each email to avoid issues with sending too quickly
            time.sleep(2)
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()

# HTML email body
html_body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {font-family: Arial, sans-serif; color: #333;}
        .container {width: 90%; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 10px; border: 1px solid #ddd;}
        h2 {color: #0056b3; font-size: 24px; margin-bottom: 20px;}
        p {font-size: 16px; line-height: 1.6;}
        .footer {margin-top: 20px; font-size: 14px; color: #555;}
        .icons {margin-top: 10px;}
        .icon-button {
            text-decoration: none;
            margin-right: 20px;
            font-size: 16px;
            color: #0056b3;
            vertical-align: middle;
        }
        .icon-button img {
            width: 24px;
            height: 24px;
            vertical-align: middle;
            margin-right: 5px;
        }
        .contact-icon {
            width: 20px;
            height: 20px;
            vertical-align: middle;
            margin-right: 8px;
        }
        .profile-image {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-bottom: 20px;
        }
        .cv-button {
            display: inline-block;
            padding: 10px 20px;
            margin-top: 20px;
            font-size: 16px;
            color: #fff;
            background-color: #0056b3;
            border-radius: 5px;
            text-decoration: none;
        }
        .cv-button:hover {
            background-color: #004494;
        }
        .header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .contact-info {
            margin-left: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Application for Software Engineer Position</h2>
        <div class="header">
            <img src="https://i.imgur.com/AOdd7TN.png" alt="Mahmoud Dawood" class="profile-image">
            <div class="contact-info">
                <p><strong>Mahmoud Dawood</strong></p>
                <p><strong>GPA: 90</strong></p>
                <p>
                    <img src="https://img.icons8.com/material-outlined/24/phone.png" alt="Phone" class="contact-icon">Phone: 054-8633751<br>
                    <img src="https://img.icons8.com/material-outlined/24/email.png" alt="Email" class="contact-icon">Email: <a href="mailto:mahmmodgkj@gmail.com">mahmmodgkj@gmail.com</a>
                </p>
            </div>
        </div>
        <p>Dear Hiring Manager,</p>
        <p>
            My name is Mahmoud Dawood, a recent Software Engineering graduate from Azrieli College of Engineering. I am eager to apply for the Software Engineer role at your esteemed company.
        </p>
        <p>
            I have hands-on experience with a wide range of technologies including <strong>C++, Python, Java, JavaScript, React, Docker,</strong> and <strong>AWS</strong>. My final project, <strong>Fast Fix</strong>, was a MERN stack application supporting real-time chat and multilingual functionality, demonstrating my ability to build complex, user-focused solutions.
        </p>
        <p>
            I also bring strong leadership and mentoring skills, having guided peers and led teams in various projects. I thrive in dynamic environments and am committed to continuous learning and professional growth.
        </p>
        <p>
           If you can help me in any way or need further information, <strong>please feel free to reply to this email</strong>.
        </p>
        <a href="https://www.dropbox.com/scl/fi/6u3kpurahbnzrzjskj7po/cv.pdf?rlkey=ajs66eko53vuw6646jp1cre79&st=nq81txzk&dl=0" class="cv-button" target="_blank">View My CV</a>
        <div class="icons">
            <a href="https://www.linkedin.com/in/mahmoud-dawood-7b4b0724a" target="_blank" class="icon-button">
                <img src="https://img.icons8.com/material-outlined/24/linkedin.png" alt="LinkedIn"> LinkedIn
            </a>
            <a href="https://github.com/MahmoudDawoodSWE" target="_blank" class="icon-button">
                <img src="https://img.icons8.com/material-outlined/24/github.png" alt="GitHub"> GitHub
            </a>
        </div>
    </div>
</body>
</html>
"""

# Usage
# Replace with your list of recipient emails
email_list = [mahmmodgkj@gmail.com,mahmmodgkj@gmail.com]

send_email("Application for Software Engineer Position", html_body, email_list)
