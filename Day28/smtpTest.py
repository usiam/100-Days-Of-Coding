import smtplib

myEmail = 'uzairt321@gmail.com'
password = "Fire@1212"

# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=myEmail, password=password)
#
# connection.sendmail(from_addr=myEmail,
#                     to_addrs='usiam@u.rochester.edu',
#                     msg='Subject:Test Email\n\nThis is the content')
# connection.close()

with smtplib.SMTP('smtp.gmail.com') as connection: # Dont have to close if we do this way
    connection.starttls()
    connection.login(user=myEmail, password=password)

    connection.sendmail(from_addr=myEmail,
                        to_addrs='usiam@u.rochester.edu',
                        msg='Subject:Test Email\n\nThis is the content')