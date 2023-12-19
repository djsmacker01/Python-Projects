# When Passing a date and time object
from datetime import datetime
from datetime import timedelta

# dt = datetime.datetime.strptime("2023-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
# print(dt)
# Add 1 day to the current date


current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

new_datetime = current_datetime + timedelta(days=1)
print("New Date and Time:", new_datetime)