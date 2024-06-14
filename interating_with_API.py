import requests

# This is my company APIs website
responds = requests.get('https://randomuser.me/api')
# the moment you run the print it will return successfull status code which is 200 sir

# print(responds.status_code)
print(responds.json)

#run the json in terminal with 'python web_scraping.py'