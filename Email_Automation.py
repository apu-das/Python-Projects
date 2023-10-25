import smtplib

to = input("Enter the mail address of the receiver:- ")

message = input("Enter the message:- ")

def sendEmail(to, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('senderemail', 'password')
    server.mail('senderemail' , to, message)
    server.close
sendEmail(to, message)
