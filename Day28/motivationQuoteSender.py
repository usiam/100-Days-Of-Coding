import smtplib, datetime as dt, random

now = dt.datetime.now()
if now.weekday() == 3:
    with open('quotes.txt') as file:
        quotes = file.readlines()
        motivationalQuote = random.choice(quotes)
        print(motivationalQuote)

myEmail = 'uzairt321@gmail.com'
myPassword = "Fire@1212"

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=myEmail, password=myPassword)
    connection.sendmail(from_addr=myEmail, to_addrs='usiam@u.rochester.edu',
                        msg=f"Subject: Motivational Quote of The Week\n\n{motivationalQuote}")
