import pandas
import smtplib
import datetime as dt
import random

test_email = "testhuman00001@gmail.com"
password = "random_letters"

birthdays_list = pandas.read_csv("birthdays.csv")
birthdays = birthdays_list.to_dict(orient="records")
print(birthdays[0])

now = dt.datetime.now()
month = now.month
day = now.day
print(day)
print(month)
for person in birthdays:
    if person["month"] == month and person["day"] == day:
        choice = random.randint(1, 3)
        with open(f"letter_templates/letter_{choice}.txt") as letter:
            letter_u = letter.read()
            p_letter = letter_u.replace("[NAME]", person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=test_email, password=password)
            connection.sendmail(
                from_addr=test_email, 
                to_addrs=person["email"],
                msg=f"Subject: Happy Birthday!!!\n\n{p_letter}"
            )





