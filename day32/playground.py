
import datetime as dt
import pandas as pd
import smtplib, random

my_email = "amber.quynh.nguyen@gmail.com"
password = "hzbmogqdnuettarr"
today = dt.datetime.now()
birthday_file = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row['month'],data_row['day']): data_row for (index,data_row) in birthday_file.iterrows()}
birthday_person = birthday_dict[(12,21)]
print(birthday_person["name"])