# Example data for a user, the time of their visit and the site they accessed.
# Print a log message with the username, url, and timestamp replaced with values from the appropriate variables

import datetime as dt

username = "User1"
timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
url = "https://www.youtube.com/"

# print a log message using the variables above.
# The message should have the output format similar to this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print(username + ' accessed the site ' + url + ' at ' + str(timestamp) + '.')
