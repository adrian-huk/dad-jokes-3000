import requests
from termcolor import colored
from random import choice
from pyfiglet import Figlet

f = Figlet(font='slant')
print(colored((f.renderText("DAD JOKES 3000")), "red"))

user_input = input("Let me tell you a joke! Choose a topic: ")

url = "https://icanhazdadjoke.com/search"

topic = {'term': user_input}
r = requests.get(url, headers={"accept": "application/json"}, params=topic)
data = r.json()

answer = "y"
while answer == "y":
    if len(data["results"]) == 0:
        print(f''' There's no such a topic!''')
        break
    else:
        random_joke_num = choice(range(0, len(data["results"])))
        print(f''' I have {len(data["results"])} jokes available. Here's one:''')
        print(data["results"][random_joke_num].get("joke"))
        answer = input("Do you want to hear another joke? (y/n)")
