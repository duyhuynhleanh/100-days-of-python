import datetime as dt
import smtplib
import pandas
import random

gmail_email = "kemjau2032@gmail.com"
gmail_password = "gld9d038"
yahoo_email="kemjau2032@yahoo.com"
yahoo_mail = "cwgqwnvtjuhldxhj"

today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=gmail_email, password=gmail_password)
        connection.sendmail(from_addr=gmail_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday! \n\n {contents}".encode("utf8"))



