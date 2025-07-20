import smtplib, random
import datetime as dt


my_email = "your_email"
password = "enter_your_pass_here"
current_day = dt.datetime.now().weekday()

if current_day == 6:
    with open("quotes.txt") as quote_file:
        quotes_list = quote_file.read().splitlines()
        quote_of_the_day = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="receiver_email", 
                            msg=f"Subject:Motivational Quote\n\n{quote_of_the_day}")

