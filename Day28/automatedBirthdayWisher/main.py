import smtplib, datetime as dt, pandas as pd, random

myEmail = 'uzairt321@gmail.com'
myPass = 'passhere'
letterTemplates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
now = dt.datetime.now()
nowMD = (now.month, now.day) # now month day (nowMD)

data = pd.read_csv('birthdays.csv')
bdayDict = {(dataRow.month, dataRow.day): dataRow for (ind, dataRow) in data.iterrows()}

if nowMD in bdayDict:
    bdayPerson = bdayDict[nowMD]
    with open(f"./letter_templates/{random.choice(letterTemplates)}") as file:
        letter = file.read()
        birthdayWish = letter.replace('[NAME]', bdayPerson['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=myEmail, password=myPass)
        connection.sendmail(from_addr=myEmail, to_addrs=bdayPerson['email'],
                            msg=f"Subject: HAPPY BIRTHDAY <3\n\n{birthdayWish}")

# you can put this code in the cloud on https://www.pythonanywhere.com/ to schedule a task at any UTC time  and
# automate the whole process
