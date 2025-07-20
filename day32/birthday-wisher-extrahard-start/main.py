##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import smtplib, random

my_email = "your_email"
password = "enter_your_password_here"
today = dt.datetime.now()
birthday_file = pd.read_csv("birthdays.csv")
matches_today = birthday_file[(birthday_file.day == today.day) & (birthday_file.month == today.month)]

if not matches_today.empty:
    names = matches_today['name'].tolist()
    emails = matches_today['email'].tolist()
    for name, email in zip(names, emails):
        random_letter_number = random.randint(1,3)
        with open(f"letter_templates/letter_{random_letter_number}.txt") as letter:
            letter_content = letter.read()
            new_letter = letter_content.replace("[NAME]",f"{name}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=email, 
                                msg=f"Subject:Happy Birthday!!\n\n{new_letter}")


