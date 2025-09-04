from datetime import datetime, timedelta

today = datetime.now()
targeted_weekdays = [1,3]
targeted_weekdays_in_datetime = [today+timedelta(days=((weekday-today.weekday() +7)%7) or 7) for weekday in targeted_weekdays]
formatted_weekdays =[weekday.strftime("%a %b %d") for weekday in targeted_weekdays_in_datetime]

print(formatted_weekdays)

# tuesday = today + timedelta(days=days_ahead_for_each_target_weekdays)
# formatted_days = tuesday.strftime("%a %b %d")

