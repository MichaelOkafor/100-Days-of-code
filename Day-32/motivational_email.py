import smtplib
import datetime as dt
import random

MY_EMAIL = "michaelokafor091@gmail.com"
PASSWORD = "okafor123"

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 0:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp@gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Omichael091@outlook.com",
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )
