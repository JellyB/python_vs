
# TO DO:
# 1. Have display_weather print the weather report.
# 2. Handle network errors by printing a friendly message.
#
# To test your code, open a terminal below and run:
#   python3 weather.py


# import requests

# API_ROOT = 'https://www.metaweather.com'
# API_LOCATION = '/api/location/search/?query='
# API_WEATHER = '/api/location/'  # + woeid

# def fetch_location(query):
#     return requests.get(API_ROOT + API_LOCATION + query).json()

# def fetch_weather(woeid):
#     return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

# def display_weather(weather):
#     print(f"Weather for {weather['title']}:")
#     print("Replace this message with the weather report!")

# def disambiguate_locations(locations):
#     print("Ambiguous location! Did you mean:")
#     for loc in locations:
#         print(f"\t* {loc['title']}")

# def weather_dialog():
#     where = ''
#     while not where:
#         where = input("Where in the world are you? ")
#     locations = fetch_location(where)
#     if len(locations) == 0:
#         print("I don't know where that is.")
#     elif len(locations) > 1:
#         disambiguate_locations(locations)
#     else:
#         woeid = locations[0]['woeid']
#         display_weather(fetch_weather(woeid))


# if __name__ == '__main__':
#     while True:
#         weather_dialog()


# import requests
# try:
#     r = requests.get('http://udacity.com')
#     print(r.status_code)
# except requests.exceptions.ConnectionError:
#     print('Could not connect to server.')


# try:
#     r = requests.get("https://www.udacity.com")
# except NameError:
#     print("Did you forget to import the requests module?")

# try:
#     print(r.text)
# except NameError:
#     print("There seems to be a NameError; r is not defined!")

# string = 'short'
# try:
#     for letter in range(6):
#         print(string[letter])
# except IndexError:
#     print("Did you try to index past the end of the string?")

# print("Woohoo! You got them all!")


# import requests

# # print(requests.get('https://api.github.com/events'))
# # print(requests.get('https://api.github.com/eventsblargh'))

# r = requests.get('http://localhost:9999/secret')
# print(r.status_code)
# print(r.text)