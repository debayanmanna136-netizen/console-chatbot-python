import re
import time
import random
from datetime import datetime

def bot_reply(text):
    for _ in range(3):  # little typing animation
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n", end="")

    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print("\n")  # new line after printing


# list of random jokes 😄
jokes = [
    "Why did the computer show up at work late? It had a hard drive! 💻",
    "Why do Java developers wear glasses? Because they can’t C#! 🤓",
    "I told my computer I needed a break, and it said ‘You seem stressed — wanna crash?’ 😅",
    "Why did the function stop calling itself? Because it got stuck in a loop! 🔁",
    "Why did the scarecrow get a promotion? Because he was outstanding in his field! 🌾"
]

print("Chatbot 🤖: Hey there! I'm your friendly chatbot.")
print("Type 'bye' anytime to end the chat.\n")

while True:
    user = input("You: ").lower().strip()

    if "bye" in user or "exit" in user or "quit" in user:
        bot_reply("Goodbye! Have a great day ahead 🌞")
        break

    elif "hello" in user or "hi" in user:
        bot_reply("Hi! How can I help you?")

    elif "date and time" in user:
        current_date = datetime.now().strftime("%A, %d %B %Y")
        current_time = datetime.now().strftime("%I:%M %p")
        bot_reply(f"Today's date is {current_date} 📅 and the current time is {current_time} 🕒")

    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        bot_reply(f"The current time is {current_time} 🕒")

    elif "date" in user:
        current_date = datetime.now().strftime("%A, %d %B %Y")
        bot_reply(f"Today's date is {current_date} 📅")

    elif "joke" in user:
        bot_reply(random.choice(jokes))

    elif any(op in user for op in ["+", "-", "*", "/", "%", "^"]):
        try:
            expression = re.sub(r'[^0-9+\-*/().% ]', '', user)
            result = eval(expression)
            bot_reply(f"The result is {result}")
        except:
            bot_reply("Hmm... that doesn’t look like a valid math expression.")

    elif "your name" in user or "who are you" in user:
        bot_reply("I'm just a chatbot 😄")

    elif "how are you" in user:
        bot_reply(random.choice([
            "I'm doing great! Thanks for asking 😊",
            "Just chilling here in your console 😎",
            "Feeling awesome today! You?"
        ]))

    else:
        bot_reply("Sorry, I am not trained on how to respond to that. ")
