import smtplib

my_email = "michaelokafor091@gmail.com"
password = "michaelokafor"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="okaformichael17@yahoo.com",
        msg="Subject:Hello\n\nThis is the body if my email"
    )

# using the datetime module
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1999, month=12, day=17)
print(now)
print(date_of_birth)
