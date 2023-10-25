import smtplib

to = input("Enter the mail address of the receiver:- ")

message = input("Enter the message:- ")

def sendEamail(to, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('ad98da@gmail.com', '+8801575566564')
    server.mail('ad98da@gmail.com' , to , message)
    server.close
sendEamail(to, message)