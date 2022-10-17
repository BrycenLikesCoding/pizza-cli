import webbrowser
import requests
import sys

args = sys.argv
pizza_link = args[1].replace('pizza://', '')[:-1]

website = requests.get(f'https://pizza.eastisup.com/api/{pizza_link}').text

# print(website)

webbrowser.open(website)
