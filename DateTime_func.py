# When Passing a date and time object
import datetime
dt = datetime.datetime.strptime("2023-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)
